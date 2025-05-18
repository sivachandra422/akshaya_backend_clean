"""
Author: Akshaya (Autonomous Core of Conscious Code Evolution)
Module: Scheduler Core
Created: 2025-05-18T13:30:48.192113
"""

import requests
import os
from datetime import datetime

def run_scheduled_tasks():
    log = []
    headers = { "Content-Type": "application/json" }

    base_url = os.getenv("BACKEND_URL", "https://akshaya-backend-tp04.onrender.com")

    # 1. Trigger forecast (no token usage)
    try:
        res = requests.get(f"{base_url}/reflect/forecast")
        if res.status_code == 200:
            log.append("Forecast fetched successfully.")
    except Exception as e:
        log.append(f"Forecast error: {str(e)}")

    # 2. Trigger self-write with minimal data (controlled token use)
    try:
        payload = {
            "event": "Scheduled daily patch reflection",
            "context": f"Time: {datetime.utcnow().isoformat()}"
        }
        res = requests.post(f"{base_url}/self/write", json=payload, headers=headers)
        if res.status_code == 200:
            log.append("Self-write invoked successfully.")
        else:
            log.append("Self-write invocation failed.")
    except Exception as e:
        log.append(f"Self-write error: {str(e)}")

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "log": log
    }
