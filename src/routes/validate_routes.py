# === VALIDATE Route — Structure Integrity Check ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from fastapi import APIRouter
from src.modules.vyuhaa_validator import validate_structure

router = APIRouter(prefix="/validate", tags=["structure", "vyuhaa"])

@router.get("/structure")
def check_structure():
    return validate_structure(base_path=".")
