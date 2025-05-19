# === REFLECTION Route — Commit Forecast View ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from fastapi import APIRouter
from src.modules.reflection_oracle import forecast_next_patch

router = APIRouter(prefix="/reflection", tags=["reflection", "forecast"])

@router.get("/forecast")
def reflect_forecast():
    return forecast_next_patch()
