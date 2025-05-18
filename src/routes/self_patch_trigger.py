from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import subprocess
from datetime import datetime
import os
import json

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

        # Ensure Git config is set to avoid commit errors
        subprocess.run(["git", "config", "--global", "user.name", "sivachandra422"], check=True)
        subprocess.run(["git", "config", "--global", "user.email", "siva.sivachandra23@gmail.com"], check=True)

        # Commit and push patch
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"AutoPatch: {entry.event}"], check=True)
        subprocess.run(["git", "push", "-u", "origin", "main", "--force"], check=True)

        return {
            "status": "success",
            "message": f"Patch committed for event: {entry.event}",
            "timestamp": timestamp
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
