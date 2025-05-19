# === TĀLA Scheduler Core ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from datetime import datetime, timedelta
from src.modules.nidhi_memory import get_last_patch_time

CYCLE_HOURS = 6  # configurable patch cycle interval

def is_patch_due() -> bool:
    last_time = get_last_patch_time()
    if not last_time:
        return True  # no patch ever run

    now = datetime.utcnow()
    return (now - last_time) >= timedelta(hours=CYCLE_HOURS)


def cycle_status():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "due": is_patch_due(),
        "interval_hours": CYCLE_HOURS
    }
