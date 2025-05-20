from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

# Placeholder for latest reflection
latest_thought = {
    "summary": "Akshaya is stable and evolving.",
    "insight": "Latest patch cycle completed successfully.",
    "timestamp": datetime.utcnow().isoformat()
}

@router.get("/status/thought")
def get_thought():
    return latest_thought