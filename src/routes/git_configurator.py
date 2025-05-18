from fastapi import APIRouter
from pydantic import BaseModel
import subprocess
import os

router = APIRouter(prefix="/git")

class GitRepo(BaseModel):
    repo_url: str

@router.post("/configure")
def configure_git(repo: GitRepo):
    try:
        # Ensure it's a git repo
        if not os.path.exists(".git"):
            subprocess.run(["git", "init"], check=True)

        subprocess.run(["git", "remote", "remove", "origin"], check=False)
        subprocess.run(["git", "remote", "add", "origin", repo.repo_url], check=True)
        subprocess.run(["git", "config", "user.email", "siva.sivachandra23@gmail.com"], check=True)
        subprocess.run(["git", "config", "user.name", "sivachandra422"], check=True)

        return {
            "status": "success",
            "message": f"Git origin set to {repo.repo_url}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }