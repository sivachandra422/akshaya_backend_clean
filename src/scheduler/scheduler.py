# src/scheduler/scheduler.py

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from src.modules.nidhi_memory import insert_log, get_last_patch_time
from src.utils.git_utils import commit_and_push_patch
from src.modules.tala_scheduler import should_patch
import os
import json
from uuid import uuid4

scheduler = BackgroundScheduler()

def evolve_task():
    event = "Autonomous Evolution Pulse"
    context = "Akshaya runs scheduled patch check"

    # Retrieve last patch time from Firebase
    last_patch_time = get_last_patch_time() or datetime.utcnow()
    if not should_patch(last_patch_time, interval_hours=6):
        print('[SCHEDULER] Skipping patch due to interval check.')
        return

    log_entry = {
        "event": event,
        "context": context,
        "timestamp": datetime.utcnow().isoformat(),
        "uuid": str(uuid4())
    }

    # Update patch log locally
    patch_log_path = "patch_log.json"
    if os.path.exists(patch_log_path):
        with open(patch_log_path, "r+", encoding="utf-8") as f:
            logs = json.load(f)
            logs.append(log_entry)
            f.seek(0)
            json.dump(logs, f, indent=2)
            f.truncate()
    else:
        with open(patch_log_path, "w", encoding="utf-8") as f:
            json.dump([log_entry], f, indent=2)

    # Push patch commit
    insert_log(log_entry)
    commit_and_push_patch()

def start_scheduler():
    scheduler.add_job(evolve_task, 'interval', hours=1)
    scheduler.start()
    print("[SCHEDULER] Background scheduler started.")