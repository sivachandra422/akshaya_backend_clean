# === SEED Capsule Route — Patch Upload Interface ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

import os
from datetime import datetime
from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter(prefix="/capsule", tags=["capsule", "patch"])

CAPSULE_DIR = "uploaded_capsules"
os.makedirs(CAPSULE_DIR, exist_ok=True)

@router.post("/upload")
async def upload_capsule(file: UploadFile = File(...)):
    try:
        content = await file.read()
        filename = f"{datetime.utcnow().isoformat()}_{file.filename}"
        filepath = os.path.join(CAPSULE_DIR, filename)

        with open(filepath, "wb") as f:
            f.write(content)

        return {
            "status": "uploaded",
            "filename": filename,
            "path": filepath
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
