# src/modules/nidhi_memory.py
from typing import Dict
from datetime import datetime
from src.modules.firebase_connector import init_firestore

db = init_firestore()

def insert_log(entry: Dict):
    """
    Internal log writer for structured event objects.
    """
    try:
        if not isinstance(entry, dict):
            raise ValueError("Log entry must be a dictionary.")

        # Add timestamp
        entry["timestamp"] = datetime.utcnow().isoformat()
        print("[LOGGING] insert_log():", entry)
        db.collection("akshaya_seed_logs").add(entry)
        print("[SUCCESS] Log entry inserted.")
        return True

    except Exception as e:
        print(f"[ERROR] insert_log() failed: {str(e)}")
        raise e


def store_log(event: str, context: str):
    """
    External API method to log an event with context string.
    """
    log_entry = {
        "event": event,
        "context": context,
        "timestamp": datetime.utcnow().isoformat()
    }
    print("[LOGGING] store_log():", log_entry)
    db.collection("akshaya_seed_logs").add(log_entry)
    return {"status": "logged", "entry": log_entry}


def get_all_logs():
    """
    Fetches all log entries from Firestore.
    """
    logs_ref = db.collection("akshaya_seed_logs")
    docs = logs_ref.stream()
    return [doc.to_dict() for doc in docs]