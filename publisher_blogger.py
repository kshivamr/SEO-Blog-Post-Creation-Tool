from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import os

SCOPES = ["https://www.googleapis.com/auth/blogger"]


def get_service():
    creds = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            "client_secret.json", SCOPES
        )
        creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("blogger", "v3", credentials=creds)
    return service


def publish_post(blog_id, title, content):
    service = get_service()

    body = {
        "kind": "blogger#post",
        "title": title,
        "content": content
    }

    post = service.posts().insert(
        blogId=blog_id,
        body=body,
        isDraft=False
    ).execute()

    return post["url"]
