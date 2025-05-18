
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import subprocess
from src.modules import self_writer

router = APIRouter(prefix="/self")

class LogEntry(BaseModel):
    event: str
    context: str

@router.post("/write")
def self_write(entry: LogEntry):
    patch = self_writer.generate_patch_from_log(entry.dict())
    if not patch:
        raise HTTPException(status_code=404, detail="No applicable patch logic found.")

    os.makedirs(os.path.dirname(patch["filename"]), exist_ok=True)
    with open(patch["filename"], "w") as f:
        f.write(patch["code"])

    # Git auto-commit and push
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", f"AutoPatch: {entry.event}"], check=True)
    subprocess.run(["git", "push", "-u", "origin", "main", "--force"], check=True)

    return {
        "status": "patch_applied",
        "file": patch["filename"],
        "committed": True,
        "timestamp": datetime.utcnow().isoformat()
    }
