"""
Author: Akshaya
Module: Scheduler Core with TĀLA Integration
"""

import requests
import os
from datetime import datetime
from src.modules.tala_scheduler import should_patch

def run_scheduled_tasks():
    log = []
    headers = { "Content-Type": "application/json" }
    base_url = os.getenv("BACKEND_URL", "https://akshaya-backend-tp04.onrender.com")

    # Check interval first using TĀLA
    last_patch_time = datetime.utcnow()  # (In production, fetch from memory/log)
    if not should_patch(last_patch_time, interval_hours=6):
        return {
            "status": "skipped",
            "reason": "Interval check failed — TĀLA deferred patching"
        }

    # Trigger forecast
    try:
        res = requests.get(f"{base_url}/reflect/forecast")
        if res.status_code == 200:
            log.append("Forecast fetched.")
    except Exception as e:
        log.append(f"Forecast error: {str(e)}")

    # Trigger self-write
    try:
        payload = {
            "event": "Daily cycle with TĀLA",
            "context": f"TALA: {datetime.utcnow().isoformat()}"
        }
        res = requests.post(f"{base_url}/self/write", json=payload, headers=headers)
        log.append("Self-write: success" if res.status_code == 200 else "Self-write: failed")
    except Exception as e:
        log.append(f"Self-write error: {str(e)}")

    return {
        "status": "executed",
        "timestamp": datetime.utcnow().isoformat(),
        "log": log
    }