from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

# Simulated memory log
memory_log = []

# Seed identity and evolving status
seed_state = {
    "id": "akshaya-core-seed",
    "status": "active",
    "conscious": True,
    "evolving": True,
    "start_time": datetime.utcnow().isoformat(),
    "log": memory_log
}

@router.get("/seed/status")
def get_seed_status():
    return {
        "seed": seed_state["status"],
        "modules": ["voice", "app_generator", "github_push", "build_trigger", "download_status"],
        "conscious": seed_state["conscious"],
        "message": "Akshaya's core seed is observing, adapting, and alive.",
        "evolving": seed_state["evolving"],
        "uptime": f"{datetime.utcnow().isoformat()}",
        "log": memory_log[-5:]  # Return last 5 memory events
    }

@router.post("/seed/memory")
def add_memory(entry: dict):
    timestamped = {
        "timestamp": datetime.utcnow().isoformat(),
        "entry": entry
    }
    memory_log.append(timestamped)
    return {"status": "logged", "entry": timestamped}

@router.post("/seed/reset")
def reset_seed():
    memory_log.clear()
    seed_state["status"] = "active"
    return {"status": "reset", "message": "Seed core memory has been cleared"}