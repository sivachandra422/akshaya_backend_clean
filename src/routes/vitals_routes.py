from fastapi import APIRouter
import time
import psutil
import platform
from datetime import datetime

router = APIRouter()

start_time = time.time()

@router.get("/status/vitals")
def get_vitals():
    uptime = time.time() - start_time
    return {
        "cpu_usage": psutil.cpu_percent(interval=0.5),
        "memory_usage": psutil.virtual_memory().percent,
        "uptime": f"{uptime:.2f} seconds",
        "platform": platform.system(),
        "status": "alive"
    }