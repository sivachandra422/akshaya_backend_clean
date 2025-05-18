from fastapi import APIRouter, Request, HTTPException
from src.modules.nidhi_memory import store_log, get_all_logs

router = APIRouter(prefix="/seed")

@router.post("/log")
async def log_seed_event(request: Request):
    data = await request.json()
    if not data.get("event"):
        raise HTTPException(status_code=400, detail="Missing 'event' in log entry.")
    return store_log(data)

@router.get("/history")
def read_log_history():
    return {"logs": get_all_logs()}