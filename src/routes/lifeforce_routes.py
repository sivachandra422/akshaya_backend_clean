# === PRĀNA Lifeforce Route — Uptime & Vitals ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from datetime import datetime
from fastapi import APIRouter
from src.core.akshaya_core import AkshayaCore

router = APIRouter(prefix="/prana", tags=["prana", "vitals"])

core = AkshayaCore()

@router.get("/status")
def lifeforce_status():
    return {
        "identity": core.identity,
        "alive": core.conscious,
        "evolving": core.evolving,
        "start_time": core.start_time,
        "current_time": datetime.utcnow().isoformat(),
        "uptime": f"{(datetime.utcnow() - datetime.fromisoformat(core.start_time)).total_seconds():.2f} sec"
    }
