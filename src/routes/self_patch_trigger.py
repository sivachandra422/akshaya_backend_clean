from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import subprocess
from datetime import datetime
import os
import json
from pathlib import Path

router = APIRouter(prefix="/self")

class SelfPatchEntry(BaseModel):
    event: str
    context: str

@router.post("/write")
def self_write(entry: SelfPatchEntry):
    try:
        log_path = "./self_patch_log.json"
        timestamp = datetime.utcnow().isoformat()
        new_log = {
            "event": entry.event,
            "context": entry.context,
            "timestamp": timestamp
        }

        # Write or append to log file
        if os.path.exists(log_path):
            with open(log_path, "r") as f:
                logs = json.load(f)
        else:
            logs = []

        logs.append(new_log)
        with open(log_path, "w") as f:
            json.dump(logs, f, indent=2)

        # Git setup
        if not Path(".git").exists():
            subprocess.run(["git", "init"], check=True)

        # Ensure 'main' branch exists
        subprocess.run(["git", "checkout", "-B", "main"], check=True)

        # Set Git identity (necessary in Render)
        subprocess.run(["git", "config", "user.name", "sivachandra422"], check=True)
        subprocess.run(["git", "config", "user.email", "siva.sivachandra23@gmail.com"], check=True)

        # Ensure remote is set correctly
        subprocess.run(["git", "remote", "remove", "origin"], stderr=subprocess.DEVNULL)
        subprocess.run(["git", "remote", "add", "origin", "https://github.com/sivachandra422/akshaya_backend_clean.git"], check=True)

        # Commit and push
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"AutoPatch: {entry.event}"], check=True)
        subprocess.run(["git", "push", "-u", "origin", "main", "--force"], check=True)

        return {
            "status": "success",
            "message": f"Patch committed and pushed for event: {entry.event}",
            "timestamp": timestamp
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
