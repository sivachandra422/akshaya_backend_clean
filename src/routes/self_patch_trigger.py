from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from src.modules.git_utils import commit_and_push_patch
from src.modules.nidhi_memory import insert_log

router = APIRouter(prefix="/self")

class SelfPatchRequest(BaseModel):
    event: str
    context: str  # must be named 'context' to match your POST

@router.post("/write")
def self_patch(req: SelfPatchRequest):
    try:
        print(f"[PATCH] Received self-patch trigger: {req.event} - {req.context}")

        # Commit patch to GitHub
        commit_msg = f"{req.event} — {req.context}"
        commit_and_push_patch(commit_msg)

        # Store event in Firestore
        log_entry = {
            "event": req.event,
            "context": req.context
        }
        insert_log(log_entry)

        return {
            "status": "success",
            "message": f"Patch committed and pushed for event: {req.event}",
            "timestamp": datetime.utcnow().isoformat()
        }

    except Exception as e:
        print(f"[ERROR] Self-patch failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))