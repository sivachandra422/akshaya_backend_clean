# === GitHub Push Utility Route ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

import base64
import os
import requests
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/github", tags=["github"])

REPO = os.getenv("GITHUB_REPO_NAME")
USER = os.getenv("GITHUB_USERNAME")
TOKEN = os.getenv("GITHUB_TOKEN")
BRANCH = "main"

def _github_headers():
    return {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

@router.post("/push")
def push_file(body: dict):
    path = body.get("path")
    message = body.get("message", "Akshaya: auto commit")
    content = body.get("content")

    if not (REPO and USER and TOKEN):
        raise HTTPException(status_code=500, detail="Missing GitHub credentials")

    if not all([path, content]):
        raise HTTPException(status_code=400, detail="Missing path or content")

    url = f"https://api.github.com/repos/{USER}/{REPO}/contents/{path}"
    data = {
        "message": message,
        "content": base64.b64encode(content.encode("utf-8")).decode("utf-8"),
        "branch": BRANCH
    }

    try:
        r = requests.put(url, json=data, headers=_github_headers())
        r.raise_for_status()
        return {"status": "success", "github_response": r.json()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"GitHub push failed: {str(e)}")
