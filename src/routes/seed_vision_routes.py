# === SEED Vision Route — Long-Term Evolution Ideas ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from datetime import datetime
from fastapi import APIRouter, HTTPException
from src.modules.nidhi_memory import insert_log, get_log_history

router = APIRouter(prefix="/vision", tags=["vision", "evolution"])

@router.post("/record")
def record_vision(body: dict):
    idea = body.get("idea")
    if not idea:
        raise HTTPException(status_code=400, detail="Missing 'idea' in request")

    entry = {
        "event": "vision",
        "context": idea,
        "timestamp": datetime.utcnow().isoformat()
    }

    success = insert_log(entry)
    return {
        "status": "success" if success else "error",
        "vision": idea
    }

@router.get("/recent")
def recent_visions(limit: int = 25):
    logs = get_log_history(limit=limit)
    visions = [log for log in logs if log.get("event") == "vision"]
    return {"visions": visions}
