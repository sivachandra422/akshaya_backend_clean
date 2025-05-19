# === Scheduler Route — Manual Forecast & Patch Trigger ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from fastapi import APIRouter
from src.scheduler.scheduler_core import run_scheduled_cycle

router = APIRouter(prefix="/cycle", tags=["scheduler", "patch"])

@router.post("/trigger")
def run_cycle():
    return run_scheduled_cycle()
