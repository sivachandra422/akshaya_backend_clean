from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import subprocess
from datetime import datetime

router = APIRouter(prefix="/forge")

class ForgeRequest(BaseModel):
    app_name: str
    repo_url: str

@router.post("/apk")
def forge_apk(req: ForgeRequest):
    app_name = req.app_name.strip().replace(" ", "_")
    repo_url = req.repo_url.strip()

    repo_name = repo_url.rstrip("/").split("/")[-1]
    local_path = f"./generated/{app_name}"

    try:
        # Initialize Git repo if not already
        if not os.path.exists(os.path.join(local_path, ".git")):
            subprocess.run(["git", "init"], cwd=local_path, check=True)
            subprocess.run(["git", "remote", "add", "origin", repo_url], cwd=local_path, check=True)

        subprocess.run(["git", "add", "."], cwd=local_path, check=True)
        subprocess.run(["git", "commit", "-m", f"APK Forge {datetime.utcnow().isoformat()}"], cwd=local_path, check=True)
        subprocess.run(["git", "push", "-u", "origin", "main", "--force"], cwd=local_path, check=True)

        return {
            "status": "success",
            "message": f"{app_name} pushed for Codemagic/GitHub Actions build.",
            "repo": repo_url,
            "timestamp": datetime.utcnow().isoformat()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))