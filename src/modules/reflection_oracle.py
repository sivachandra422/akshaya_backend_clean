from datetime import datetime
from src.modules.github_commit_reader import fetch_recent_commits

def forecast_next_patch():
    commits = fetch_recent_commits()
    action_keywords = {
        "voice": "voice expansion",
        "app": "new screen generation",
        "build": "build optimization",
        "self": "enable deeper patching recursion"
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
        "predictions": suggested
    }
