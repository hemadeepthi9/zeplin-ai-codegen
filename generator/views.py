import os
import requests # type: ignore
from django.shortcuts import render # type: ignore
from .zeplin import get_image_from_url
from .ai import generate_code   # <-- your real function

OUTPUT = "output"
os.makedirs(OUTPUT, exist_ok=True)

CURRENT_HTML = None


def home(request):
    global CURRENT_HTML

    if request.method == "POST":

        action = request.POST.get("action")

        if action == "generate":

            link = request.POST["url"]

            parts = link.split("/")
            project_id = parts[4]
            screen_id = parts[6]

            img_url = get_image_from_url(project_id, screen_id)
            img = requests.get(img_url).content

            with open("screen.png", "wb") as f:
                f.write(img)

            html = generate_code("screen.png", mode="html")

            CURRENT_HTML = html

            with open(f"{OUTPUT}/index.html", "w") as f:
                f.write(html)

    
        if action == "refine" and CURRENT_HTML:

            instruction = request.POST["instruction"]

            refined_prompt = f"""
Here is the current HTML code:

{CURRENT_HTML}

User wants these changes:
{instruction}

Update the HTML accordingly.
Return full updated code only.
"""

            html = generate_code("screen.png", mode="html")  # reuse call

            CURRENT_HTML = html

            with open(f"{OUTPUT}/index.html", "w") as f:
                f.write(html)

    return render(request, "home.html", {
        "code": CURRENT_HTML
    })
