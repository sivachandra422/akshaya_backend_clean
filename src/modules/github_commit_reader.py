import requests
import os

def fetch_recent_commits(repo="sivachandra422/akshaya_backend_clean", limit=10):
    token = os.getenv("GITHUB_PAT")
    if not token:
        raise Exception("GITHUB_PAT not found in environment variables")

    url = f"https://api.github.com/repos/{repo}/commits"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    commits = [{
        "message": commit["commit"]["message"],
        "author": commit["commit"]["author"]["name"],
        "timestamp": commit["commit"]["author"]["date"]
    } for commit in data[:limit]]

    return commits
