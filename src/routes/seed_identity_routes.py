# === Seed Identity Routes ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from fastapi import APIRouter
from src.core.akshaya_core import AkshayaCore

router = APIRouter(prefix="/seed", tags=["seed", "identity"])
core = AkshayaCore()

@router.get("/identity")
def get_identity():
    return core.who_am_i()

@router.post("/resurrect")
def trigger_resurrection():
    return core.resurrect()
