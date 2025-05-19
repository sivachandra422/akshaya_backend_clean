# === Akshaya Scheduler Core ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from datetime import datetime
from src.scheduler.tala_scheduler import is_patch_due
from src.modules.reflection_oracle import forecast_next_patch
from src.modules.nidhi_memory import store_log

def run_scheduled_cycle():
    if not is_patch_due():
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "status": "skipped",
            "reason": "Patch not due"
        }

    forecast = forecast_next_patch()
    store_log("scheduler_triggered", "TĀLA initiated reflection + patch cycle")

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "status": "executed",
        "forecast_summary": forecast
    }
