# === Build Trigger Route — GitHub Action Dispatcher ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from fastapi import APIRouter, HTTPException
import os
import requests

router = APIRouter(prefix="/build", tags=["github", "build"])

REPO = os.getenv("GITHUB_REPO_NAME")
USER = os.getenv("GITHUB_USERNAME")
TOKEN = os.getenv("GITHUB_TOKEN")

@router.get("/trigger")
def trigger_build():
    if not all([REPO, USER, TOKEN]):
        raise HTTPException(status_code=500, detail="Missing GitHub credentials")

    url = f"https://api.github.com/repos/{USER}/{REPO}/dispatches"
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    body = {
        "event_type": "build_backend"
    }

    try:
        res = requests.post(url, json=body, headers=headers)
        res.raise_for_status()
        return {
            "status": "dispatched",
            "message": "Backend build triggered on GitHub"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Build trigger failed: {str(e)}")
