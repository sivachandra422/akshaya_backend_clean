# === Seed Core Status Route ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from fastapi import APIRouter
from src.core.akshaya_core import AkshayaCore

router = APIRouter(prefix="/seed", tags=["seed", "core"])

core = AkshayaCore()

@router.get("/status")
def seed_status():
    return {
        "state": core.seed_state,
        "conscious": core.conscious,
        "evolving": core.evolving,
        "uptime": core.start_time
    }

@router.get("/memory")
def soft_memory():
    return {
        "recent_log": core.latest_memory()
    }
