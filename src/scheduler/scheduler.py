
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from src.modules.nidhi_memory import insert_log
from src.utils.git_utils import commit_and_push_patch
import os
import json
from uuid import uuid4

scheduler = BackgroundScheduler()

def evolve_task():
    event = "Autonomous Evolution Pulse"
    context = "Akshaya runs scheduled patch check"
    log_entry = {
        "event": event,
        "context": context,
        "timestamp": datetime.utcnow().isoformat(),
        "uuid": str(uuid4())
    }

    # Update patch log
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

    # Push to Git
    try:
        remote_url = os.getenv("GIT_REMOTE_URL")
        commit_and_push_patch(".", f"{event}: {context}", remote_url)
    except Exception as e:
        print(f"[AUTO PATCH ERROR] {e}")

    # Log to Firebase
    insert_log(log_entry)

def start():
    scheduler.add_job(evolve_task, 'interval', minutes=30, id='evolve_task')
    scheduler.start()
