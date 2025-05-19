# === APK Forge Route — GitHub App Builder Trigger ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from fastapi import APIRouter, HTTPException
import requests
import os

router = APIRouter(prefix="/forge", tags=["apk", "github"])

GITHUB_API = "https://api.github.com"
REPO = os.getenv("GITHUB_REPO_NAME")
USER = os.getenv("GITHUB_USERNAME")
TOKEN = os.getenv("GITHUB_TOKEN")

@router.post("/trigger")
def trigger_apk_build():
    if not all([REPO, USER, TOKEN]):
        raise HTTPException(status_code=500, detail="Missing GitHub environment variables")

    url = f"{GITHUB_API}/repos/{USER}/{REPO}/dispatches"
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    body = {
        "event_type": "build_apk"
    }

    try:
        r = requests.post(url, json=body, headers=headers)
        r.raise_for_status()
        return {
            "status": "triggered",
            "message": "APK build workflow triggered on GitHub"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Trigger failed: {str(e)}")
