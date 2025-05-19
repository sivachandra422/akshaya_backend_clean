# === Reflection Oracle ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from datetime import datetime
from src.modules.github_commit_reader import fetch_recent_commits

def forecast_next_patch():
    commits = fetch_recent_commits()
    if not commits:
        return {
            "forecast_time": datetime.utcnow().isoformat(),
            "predictions": [],
            "message": "No commits found — nothing to reflect on."
        }

    action_keywords = {
        "voice": "Voice tuning or audio layer improvements",
        "build": "Deployment or CI/CD optimization required",
        "self": "Recursive patch or consciousness update",
        "emotion": "Journal or emotion model tuning",
        "scheduler": "Cycle logic review or restart needed",
        "core": "Identity or logic alignment update"
    }

    suggested = []
    for commit in commits:
        for keyword, suggestion in action_keywords.items():
            if keyword in commit["message"].lower():
                suggested.append({
                    "timestamp": commit["timestamp"],
                    "commit": commit["message"],
                    "suggested_next_action": suggestion
                })
                break

    return {
        "forecast_time": datetime.utcnow().isoformat(),
        "predictions": suggested or ["No clear actions found in commits."]
    }
