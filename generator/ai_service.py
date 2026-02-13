import base64
import os
from pathlib import Path
import requests # type: ignore

BASE_DIR = Path(__file__).resolve().parent.parent.parent
IMAGE_PATH = BASE_DIR / "screen.png"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")



def generate_from_image(image_path=IMAGE_PATH):
    with open(image_path, "rb") as f:
        img = base64.b64encode(f.read()).decode()

    payload = {
        "model": "google/gemini-2.0-flash-001",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Convert this UI to clean responsive HTML CSS"},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img}"}}
                ]
            }
        ],
        "max_tokens": 6000
    }

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    res = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        json=payload,
        headers=headers
    )

    return res.json()["choices"][0]["message"]["content"]
