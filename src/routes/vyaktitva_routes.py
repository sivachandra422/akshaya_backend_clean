# === VYAKTITVA Route — Personality Interface ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from fastapi import APIRouter
from src.modules.vyaktitva_manifestor import personality_state

router = APIRouter(prefix="/personality", tags=["vyaktitva", "personality"])

@router.get("/mode")
def current_mode():
    return personality_state()
