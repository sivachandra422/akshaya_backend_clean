from fastapi import APIRouter, HTTPException, Request
from src.modules.nidhi_memory import store_log
from src.modules.firebase_connector import db, init_firestore, firebase_initialized
from google.cloud import firestore
from datetime import datetime

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


@router.get("/seed/history")
def get_log_history():
    try:
        if not firebase_initialized:
            init_firestore()

        logs_ref = db.collection("akshaya_seed_logs").order_by("timestamp", direction=firestore.Query.DESCENDING)
        logs = logs_ref.stream()
        return [doc.to_dict() for doc in logs]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))