# === SEED Event Route — Manual Event Logger ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from datetime import datetime
from fastapi import APIRouter, HTTPException
from src.modules.nidhi_memory import insert_log

router = APIRouter(prefix="/event", tags=["seed", "event"])

@router.post("/log")
def log_custom_event(body: dict):
    event = body.get("event")
    context = body.get("context", "")

    if not event:
        raise HTTPException(status_code=400, detail="Missing 'event' field")

    entry = {
        "event": event,
        "context": context,
        "timestamp": datetime.utcnow().isoformat()
    }

    success = insert_log(entry)
    return {
        "status": "logged" if success else "failed",
        "entry": entry
    }
