
from fastapi import APIRouter
from src.core.akshaya_core import AkshayaCore

router = APIRouter()
core = AkshayaCore()

@router.get("/seed/identity")
def identity():
    return core.who_am_i()

@router.post("/seed/resurrect")
def resurrect():
    return core.resurrect()
