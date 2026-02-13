import requests # type: ignore
import base64
import os


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_code(image_path, mode="html"):

    img = base64.b64encode(open(image_path,"rb").read()).decode()

    if mode == "html":
        prompt = "Generate complete responsive HTML with CSS and JS. Return only code."
    else:
        prompt = "Generate React functional component. JSX only."

    payload = {
        "model": "google/gemini-2.0-flash-001",
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {
                    "url": f"data:image/png;base64,{img}"
                }}
            ]
        }],
        "max_tokens": 8000
    }

    r = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_KEY}",
            "Content-Type": "application/json"
        },
        json=payload
    )
    
    res = r.json()
    print("AI RESPONSE:", res)

    if "choices" in res:
        return res["choices"][0]["message"]["content"]

    if "output" in res:
        return res["output"]

    if "data" in res:
        return str(res["data"])

    return str(res)


    

