# === Seed Log Routes ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from fastapi import APIRouter
from src.modules.nidhi_memory import get_log_history, store_log

router = APIRouter(prefix="/seed", tags=["seed", "logs"])

@router.post("/log")
def log_event(body: dict):
    event = body.get("event")
    context = body.get("context", "")
    return store_log(event, context)

@router.get("/history")
def view_log_history(limit: int = 25):
    return get_log_history(limit=limit)
