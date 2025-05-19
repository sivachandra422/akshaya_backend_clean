from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
import os

from src.utils.git_utils import commit_and_push_patch
from src.modules.nidhi_memory import insert_log

router = APIRouter(prefix="/self")

class SelfPatchRequest(BaseModel):
    event: str
    context: str

@router.post("/write")
def self_patch(req: SelfPatchRequest):
    try:
        print(f"[PATCH] Self-triggered patch: {req.event} | {req.context}")

        # Set repo path and remote
        repo_path = "."  # current directory of Render deployment
        remote_url = os.getenv("GIT_REPO")
        if not remote_url:
            raise ValueError("Missing GIT_REPO environment variable")

        commit_message = f"{req.event} — {req.context}"

        # Commit + push
        commit_and_push_patch(repo_path, commit_message, remote_url)

        # Log patch event to Firestore
        log_entry = {
            "event": req.event,
            "context": req.context,
            "timestamp": datetime.utcnow().isoformat()
        }
        insert_log(log_entry)

        return {
            "status": "success",
            "message": f"Patch committed and pushed for event: {req.event}",
            "timestamp": log_entry["timestamp"]
        }

    except Exception as e:
        print(f"[PATCH ERROR] {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))