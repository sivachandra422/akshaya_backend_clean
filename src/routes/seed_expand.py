# Akshaya Seed Expand Route | Injects modular signatures into route files

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
import os

router = APIRouter()

class ExpandRequest(BaseModel):
    route_path: str  # Path to the route file to patch

@router.post("/seed/expand")
def expand_seed(req: ExpandRequest):
    route_path = req.route_path.strip()

    if not os.path.exists(route_path):
        raise HTTPException(status_code=404, detail="Route file not found")

    try:
        with open(route_path, "r") as f:
            content = f.read()

        marker = "# Akshaya.Mark"
        if marker in content:
            return {"status": "skipped", "message": "Already expanded with Akshaya mark."}

        patch = f"\n\n{marker}\n# Expanded via Akshaya Seed / VYUHAA\n"

        with open(route_path, "a") as f:
            f.write(patch)

        return {
            "status": "done",
            "message": "Patched with Akshaya mark"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))