import requests # type: ignore
import base64
import os
import re

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


PATTERN_DIR = "generator/patterns"


def load_patterns():
    texts = []
    for f in os.listdir(PATTERN_DIR):
        with open(os.path.join(PATTERN_DIR, f)) as file:
            texts.append(file.read())
    return "\n".join(texts)


def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()
    
def clean_code(raw):
    # Remove ```html or ``` or ```anything
    raw = re.sub(r"```[a-zA-Z]*", "", raw)
    raw = raw.replace("```", "")
    return raw.strip()



def call_ai(messages):
    response = requests.post(
        OPENROUTER_URL,
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:8000",
            "X-Title": "zeplin-codegen"
        },
        json={
            "model": "google/gemini-2.0-flash-001",
            "messages": messages,
            "max_tokens": 8000
        }
    )

    data = response.json()
    print("AI RESPONSE:", data)

    if "choices" in data:
        return data["choices"][0]["message"]["content"]

    return str(data)



def generate_from_image(image_path, mode="html"):
    img = encode_image(image_path)

    pattern_context = load_patterns()


    base_prompt = f"""
You are a professional UI engineer cloning a real product screen.

IMPORTANT UI STABILITY RULES:
{pattern_context}

Your goal is VISUAL FIDELITY.

STRICT RULES:
- DO NOT wrap the output in ``` or ```html.
- DO NOT use markdown.
- Return raw HTML code only.

- Match spacing exactly
- Match font hierarchy
- Match layout structure
- Do NOT redesign
- Do NOT simplify

First analyze layout grid, then generate code.

Return ONLY final working code.
"""



    if mode == "html":
        base_prompt += "Use semantic HTML with embedded CSS."
    else:
        base_prompt += "Return a React functional component using JSX and inline CSS or Tailwind."

    messages = [{
        "role": "user",
        "content": [
            {"type": "text", "text": base_prompt},
            {"type": "image_url", "image_url": {
                "url": f"data:image/png;base64,{img}"
            }}
        ]
    }]

    return call_ai(messages)



def refine_code(existing_code, user_instruction):
    refine_prompt = f"""
You are a senior frontend engineer.

Here is the current UI code:

{existing_code}

User wants these changes:
{user_instruction}

Update the code to apply changes.
Keep structure clean.
Return full updated code only.
"""

    messages = [{
        "role": "user",
        "content": refine_prompt
    }]

    return call_ai(messages)
