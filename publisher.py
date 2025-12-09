
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def publish_to_wordpress(title, content):
    url = os.getenv("WP_URL")
    username = os.getenv("WP_USERNAME")
    password = os.getenv("WP_APP_PASSWORD")

    data = {
        "title": title,
        "content": content,
        "status": "publish"
    }

    r = requests.post(url, auth=(username, password), json=data)

    try:
        return r.json().get("link", "Posted but no link returned")
    except:
        return r.text
