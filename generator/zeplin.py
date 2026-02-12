import requests

ZEPLIN_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoicGVyc29uYWxfYWNjZXNzX3Rva2VuIiwiY2xpZW50X2lkIjoiNjk4ZDkyODg3YWU4ZjY3YTdiOTE0OGRmIiwic2NvcGUiOiJhZG1pbiIsImlhdCI6MTc3MDg4NTc2OCwiZXhwIjoyMDg2NDU1MDI4LCJpc3MiOiJ6ZXBsaW46YXBpLnplcGxpbi5pbyIsInN1YiI6IjY5OGJmYjI3ODljMWY2NTUyMzEyMDZiNSIsImp0aSI6ImEwZjExMWFhLWQyYTctNDYxYy04YWFhLWE2OWFkZGU0ZWY0ZSJ9.xW7JgGlDnPzzxjBEAwcoUM-uXmQaSXYs8fmBarPsbYM"


def get_image_from_url(project_id, screen_id):

    url = f"https://api.zeplin.dev/v1/projects/{project_id}/screens/{screen_id}"

    r = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {ZEPLIN_TOKEN}",
            "Accept": "application/json"
        }
    )

    print("STATUS:", r.status_code)
    print(r.text)

    r.raise_for_status()

    return r.json()["image"]["original_url"]
