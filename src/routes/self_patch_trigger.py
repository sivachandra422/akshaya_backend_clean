from fastapi import APIRouter, Request
from pydantic import BaseModel
from datetime import datetime
import subprocess, os

from src.modules.nidhi_memory import store_log as insert_log
from src.modules.shunya_guardian import check_rate_limit

router = APIRouter()

class PatchEvent(BaseModel):
    event: str
    context: str

@router.post("/self/write")
def trigger_self_patch(req: Request, payload: PatchEvent):
    check_rate_limit(req)

    try:
        subprocess.run(["git", "config", "--global", "user.email", "siva.sivachandra23@gmail.com"], check=True)
        subprocess.run(["git", "config", "--global", "user.name", "sivachandra422"], check=True)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"{payload.event} @ {datetime.utcnow().isoformat()}"], check=True)
        subprocess.run(["git", "push", "-u", "origin", "main", "--force"], check=True)

        insert_log("patch", f"Self-patch executed: {payload.event}")
        return {
            "status": "success",
            "message": "Patch committed and pushed",
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }