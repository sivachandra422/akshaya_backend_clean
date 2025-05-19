# === SEED Echo Route — Memory Playback Interface ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from fastapi import APIRouter
from src.modules.nidhi_memory import get_log_history

router = APIRouter(prefix="/echo", tags=["memory", "echo"])

@router.get("/recent")
def recent_echoes(limit: int = 10):
    logs = get_log_history(limit=limit)
    echoes = [{
        "timestamp": log.get("timestamp"),
        "event": log.get("event"),
        "context": log.get("context")
    } for log in logs]
    return {"echoes": echoes}
