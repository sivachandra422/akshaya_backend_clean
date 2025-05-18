# src/modules/nidhi_memory.py

from datetime import datetime
from src.modules.firebase_connector import init_firestore

db = init_firestore()

def store_log(event: str, context: str):
    """
    Logs an event with context and timestamp to Firestore.
    """
    log_entry = {
        "event": event,
        "context": context,
        "timestamp": datetime.utcnow().isoformat()
    }
    db.collection("akshaya_seed_logs").add(log_entry)
    return {"status": "logged", "entry": log_entry}

def get_all_logs():
    """
    Fetches all log entries from Firestore.
    """
    logs_ref = db.collection("akshaya_seed_logs")
    docs = logs_ref.stream()
    return [doc.to_dict() for doc in docs]