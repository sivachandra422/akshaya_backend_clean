# src/modules/nidhi_memory.py
from typing import Dict
from datetime import datetime
from src.modules.firebase_connector import init_firestore
from google.cloud import firestore  # Ensure this package is installed

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
    insert_log(log_entry)

def get_last_patch_time():
    """
    Retrieve the most recent patch log timestamp from Firebase.
    """
    try:
        logs_ref = db.collection("akshaya_seed_logs").order_by("timestamp", direction=firestore.Query.DESCENDING).limit(1)
        docs = logs_ref.stream()
        for doc in docs:
            timestamp_str = doc.to_dict().get("timestamp")
            if timestamp_str:
                return datetime.fromisoformat(timestamp_str)
    except Exception as e:
        print(f"[ERROR] get_last_patch_time() failed: {str(e)}")
    return None