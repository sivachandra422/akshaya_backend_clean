# === Scheduler Route — Manual Forecast & Patch Trigger ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from fastapi import APIRouter
from src.scheduler.scheduler_core import run_scheduled_cycle
from src.modules.nidhi_memory import insert_log

router = APIRouter(prefix="/cycle", tags=["scheduler", "patch"])

@router.post("/trigger")
def run_cycle():
    result = run_scheduled_cycle()

    # Log the manual trigger as a patch cycle
    insert_log({
        "event": "manual_patch_cycle",
        "context": result,
        "source": "manual_trigger"
    })

    return {
        "status": "executed",
        "result": result
    }