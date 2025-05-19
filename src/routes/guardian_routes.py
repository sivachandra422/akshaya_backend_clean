# === GUARDIAN Route — Identity Management ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from fastapi import APIRouter, HTTPException
from src.core.akshaya_core import AkshayaCore

router = APIRouter(prefix="/guardian", tags=["guardian", "identity"])

core = AkshayaCore()

@router.get("/current")
def get_guardian():
    return {"guardian": core.guardian}

@router.post("/set")
def set_guardian(body: dict):
    name = body.get("name")
    if not name:
        raise HTTPException(status_code=400, detail="Missing 'name'")
    core.guardian = name
    return {"status": "updated", "guardian": core.guardian}
