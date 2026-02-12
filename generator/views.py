import requests, os
from django.shortcuts import render
from .zeplin import get_image_from_url
from .ai import generate_code

OUTPUT = "output"
os.makedirs(OUTPUT, exist_ok=True)

def home(request):

    if request.method == "POST":

        link = request.POST["url"]

        parts = link.split("/")
        project_id = parts[4]
        screen_id = parts[6]

        img_url = get_image_from_url(project_id, screen_id)

        img = requests.get(img_url).content
        open("screen.png","wb").write(img)

        html = generate_code("screen.png", "html")
        react = generate_code("screen.png", "react")

        open(f"{OUTPUT}/index.html","w").write(html)
        open(f"{OUTPUT}/Component.jsx","w").write(react)

        return render(request,"home.html",{
            "done":True
        })

    return render(request,"home.html")
