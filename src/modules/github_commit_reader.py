# === GitHub Commit Reader ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

import os
import requests
from datetime import datetime

GITHUB_API = "https://api.github.com"
REPO = os.getenv("GITHUB_REPO_NAME")
USER = os.getenv("GITHUB_USERNAME")
TOKEN = os.getenv("GITHUB_TOKEN")

def fetch_recent_commits(limit: int = 10):
    if not (REPO and USER and TOKEN):
        print("[ERROR] GitHub credentials not set.")
        return []

    url = f"{GITHUB_API}/repos/{USER}/{REPO}/commits"
    headers = {"Authorization": f"token {TOKEN}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        commits = response.json()

        return [{
            "message": commit["commit"]["message"],
            "timestamp": commit["commit"]["author"]["date"]
        } for commit in commits[:limit]]

    except Exception as e:
        print(f"[ERROR] Failed to fetch commits: {e}")
        return []
