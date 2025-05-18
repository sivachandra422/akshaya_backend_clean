import os
import tarfile
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(prefix="/frontend")

class UIInjectRequest(BaseModel):
    app_name: str

@router.post("/init")
def inject_flutter_ui(req: UIInjectRequest):
    app_name = req.app_name.strip().replace(" ", "_")
    target_path = f"./generated/{app_name}"

    template_tar = "./frontend_template/flutter_clean_template.tar.gz"
    if not os.path.exists(template_tar):
        raise HTTPException(status_code=500, detail="Frontend template archive missing.")

    try:
        os.makedirs(target_path, exist_ok=True)
        with tarfile.open(template_tar, "r:gz") as tar:
            tar.extractall(path=target_path)

        return {
            "status": "success",
            "message": f"Flutter UI template injected into {target_path}",
            "timestamp": datetime.utcnow().isoformat()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))