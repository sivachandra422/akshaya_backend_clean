from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
import os
import json
from pathlib import Path
import subprocess

from src.utils.git_utils import commit_and_push_patch
from src.modules.nidhi_memory import insert_log

router = APIRouter(prefix="/self")

class SelfPatchRequest(BaseModel):
    event: str
    context: str

@router.post("/write")
def self_patch(req: SelfPatchRequest):
    try:
        print(f"[PATCH] Triggered: {req.event} — {req.context}")
        repo_path = "."
        remote_url = os.getenv("GIT_REMOTE_URL")
        if not remote_url:
            raise ValueError("Missing GIT_REMOTE_URL environment variable")

        commit_message = f"{req.event}: {req.context}"

        # Step 1: Ensure .git repo exists
        if not os.path.exists(os.path.join(repo_path, ".git")):
            subprocess.run(["git", "init"], cwd=repo_path, check=True)
            subprocess.run(["git", "remote", "add", "origin", remote_url], cwd=repo_path, check=True)

        # Step 2: Try patching directly
        try:
            commit_and_push_patch(repo_path, commit_message, remote_url)

        except Exception as e:
            if "nothing to commit" in str(e):
                # Fallback: write to patch_log.json
                patch_log_path = Path("patch_log.json")
                fallback_entry = {
                    "event": req.event,
                    "context": req.context,
                    "timestamp": datetime.utcnow().isoformat()
                }

                if patch_log_path.exists():
                    with patch_log_path.open("r+") as f:
                        logs = json.load(f)
                        logs.append(fallback_entry)
                        f.seek(0)
                        json.dump(logs, f, indent=2)
                        f.truncate()
                else:
                    with patch_log_path.open("w") as f:
                        json.dump([fallback_entry], f, indent=2)

                # Retry Git patch after fallback
                commit_and_push_patch(repo_path, f"{commit_message} (fallback log)", remote_url)
            else:
                raise e

        # Step 3: Log to Firebase
        insert_log({
            "event": req.event,
            "context": req.context,
            "timestamp": datetime.utcnow().isoformat()
        })

        return {
            "status": "success",
            "message": f"Patch committed and pushed for event: {req.event}",
            "timestamp": datetime.utcnow().isoformat()
        }

    except Exception as e:
        print(f"[PATCH ERROR] {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))