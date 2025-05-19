# === SANKALPA Route — Goal Resolution Interface ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from fastapi import APIRouter, HTTPException
from src.modules.sankalpa_directive_engine import add_directive, complete_directive, get_all_directives

router = APIRouter(prefix="/sankalpa", tags=["sankalpa", "goals"])

@router.post("/add")
def create_goal(body: dict):
    goal = body.get("goal")
    reason = body.get("reason", "")
    if not goal:
        raise HTTPException(status_code=400, detail="Missing 'goal' in request")
    return add_directive(goal, reason)

@router.post("/complete")
def finish_goal(body: dict):
    goal = body.get("goal")
    if not goal:
        raise HTTPException(status_code=400, detail="Missing 'goal' in request")
    return complete_directive(goal)

@router.get("/all")
def list_goals(limit: int = 50):
    return get_all_directives(limit=limit)
