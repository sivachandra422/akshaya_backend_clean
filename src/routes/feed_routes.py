from fastapi import APIRouter
from firebase_connector import get_firestore_client
from datetime import datetime

router = APIRouter()

@router.get("/status/feed")
def get_log_feed():
    db = get_firestore_client()
    logs = db.collection("seed").order_by("timestamp", direction="DESCENDING").limit(30).stream()
    return [doc.to_dict() for doc in logs]