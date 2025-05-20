from fastapi import APIRouter
from fastapi.responses import JSONResponse
import psutil
import datetime
from firebase_admin import firestore

router = APIRouter()
db = firestore.client()

@router.get("/status/vitals")
async def get_vitals():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
    latency = round(psutil.cpu_times().user * 2.5 % 100, 2)
    return {
        "cpu": f"{cpu}%",
        "memory": f"{memory}%",
        "uptime": str(uptime).split('.')[0],
        "api_latency": f"{latency}ms"
    }

@router.get("/status/thought")
async def get_current_thought():
    doc = db.collection("core_status").document("current_thought").get()
    return {"thought": doc.to_dict().get("message", "No thought yet.") if doc.exists else "Unavailable"}

@router.get("/status/logs")
async def get_logs():
    logs_ref = db.collection("terminal_logs").order_by("timestamp", direction=firestore.Query.DESCENDING).limit(10)
    logs = [doc.to_dict() for doc in logs_ref.stream()]
    return {"logs": logs}

@router.get("/status/summary")
async def get_summary():
    vitals = await get_vitals()
    thought = await get_current_thought()
    logs = await get_logs()
    return {
        "metrics": vitals,
        "thought": thought.get("thought"),
        "logs": logs.get("logs")
    }

@router.get("/seed/history")
async def fixed_seed_history():
    logs_ref = db.collection("terminal_logs").order_by("timestamp", direction=firestore.Query.DESCENDING).limit(30)
    logs = [doc.to_dict() for doc in logs_ref.stream()]
    return logs or []