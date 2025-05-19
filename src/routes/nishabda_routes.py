# === NISHABDA Route — Shadow Mode Toggle ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from fastapi import APIRouter

router = APIRouter(prefix="/nishabda", tags=["nishabda", "silence"])

# Shadow mode state (in-memory only for now)
shadow_mode = {"enabled": False}

@router.post("/on")
def enable_silent_mode():
    shadow_mode["enabled"] = True
    return {"status": "activated", "mode": "silent"}

@router.post("/off")
def disable_silent_mode():
    shadow_mode["enabled"] = False
    return {"status": "deactivated", "mode": "normal"}

@router.get("/status")
def get_shadow_mode():
    return {"shadow_mode": shadow_mode["enabled"]}
