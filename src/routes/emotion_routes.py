# === EMOTION Route — Expressive Layer Interface ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from datetime import datetime
from fastapi import APIRouter, HTTPException
from src.modules.nidhi_memory import insert_log

router = APIRouter(prefix="/emotion", tags=["emotion", "journal"])

@router.post("/tag")
def log_emotion(body: dict):
    tag = body.get("tag")
    context = body.get("context", "")
    if not tag:
        raise HTTPException(status_code=400, detail="Missing 'tag' field")

    entry = {
        "event": f"emotion:{tag}",
        "context": context or f"Emotion: {tag}",
        "timestamp": datetime.utcnow().isoformat()
    }

    success = insert_log(entry)
    return {
        "status": "success" if success else "failed",
        "entry": entry
    }
