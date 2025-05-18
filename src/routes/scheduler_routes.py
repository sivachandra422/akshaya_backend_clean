"""
Author: Akshaya
Route: /cycle/run — Executes daily scheduler tasks
"""

from fastapi import APIRouter
from src.modules.scheduler_core import run_scheduled_tasks

router = APIRouter(prefix="/cycle")

@router.get("/run")
def run_daily_cycle():
    return run_scheduled_tasks()
