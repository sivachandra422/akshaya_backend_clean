from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
import os

from src.utils.git_utils import init_git_repo_if_needed, push_changes
from src.modules.nidhi_memory import insert_log

router = APIRouter(prefix="/self")

class SelfPatchEntry(BaseModel):
    event: str
    context: str

@router.post("/write")
def trigger_self_patch(entry: SelfPatchEntry):
    try:
        # 1. Log to Firebase
        insert_log(entry.event, entry.context)

        # 2. Git operations
        repo_path = os.getcwd()
        remote_url = os.getenv("GIT_REMOTE_URL")
        if not remote_url:
            raise HTTPException(status_code=400, detail="Missing GIT_REMOTE_URL")

        init_git_repo_if_needed(repo_path, remote_url)

        commit_message = f"AutoPatch: {entry.event} - {datetime.utcnow().isoformat()}"
        push_changes(repo_path, commit_message)

        return {
            "status": "success",
            "message": f"Patch committed and pushed for event: {entry.event}",
            "timestamp": datetime.utcnow().isoformat()
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}