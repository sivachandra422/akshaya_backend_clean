# === TĀLA Route — Patch Rhythm Tracker ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from fastapi import APIRouter
from src.scheduler.tala_scheduler import cycle_status

router = APIRouter(prefix="/tala", tags=["tala", "scheduler"])

@router.get("/status")
def patch_due_status():
    return cycle_status()
