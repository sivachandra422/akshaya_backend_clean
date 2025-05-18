from fastapi import APIRouter, HTTPException, Request
from src.modules.nidhi_memory import store_log

router = APIRouter()

@router.post("/seed/log")
async def log_event(request: Request):
    try:
        payload = await request.json()
        if "event" not in payload or "context" not in payload:
            raise ValueError("Missing required keys: 'event' and 'context'.")

        result = store_log(payload["event"], payload["context"])
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))