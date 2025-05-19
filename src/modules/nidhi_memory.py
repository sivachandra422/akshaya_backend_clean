# === NIDHI Memory Ally ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from typing import Dict, List
from datetime import datetime
from google.cloud import firestore
from src.modules.firebase_connector import init_firestore

COLLECTION_NAME = "akshaya_seed_logs"
db = init_firestore()


def insert_log(entry: Dict) -> bool:
    """Insert structured log entry into Firestore."""
    try:
        if not isinstance(entry, dict):
            raise ValueError("Log entry must be a dictionary.")

        entry["timestamp"] = datetime.utcnow().isoformat()
        db.collection(COLLECTION_NAME).add(entry)
        return True

    except Exception as e:
        print(f"[ERROR] insert_log() failed: {str(e)}")
        return False


def store_log(event: str, context: str) -> Dict:
    """External API entry point to log an event and context."""
    entry = {
        "event": event,
        "context": context,
        "timestamp": datetime.utcnow().isoformat()
    }
    success = insert_log(entry)
    return {"status": "success" if success else "error", "entry": entry}


def get_last_patch_time():
    """Return timestamp of most recent patch entry."""
    try:
        logs_ref = db.collection(COLLECTION_NAME).order_by("timestamp", direction=firestore.Query.DESCENDING).limit(1)
        docs = list(logs_ref.stream())
        if docs:
            return datetime.fromisoformat(docs[0].to_dict().get("timestamp"))
        return None
    except Exception as e:
        print(f"[ERROR] get_last_patch_time(): {str(e)}")
        return None


def get_log_history(limit: int = 100) -> List[Dict]:
    try:
        logs_ref = db.collection(COLLECTION_NAME).order_by("timestamp", direction=firestore.Query.DESCENDING).limit(limit)
        return [doc.to_dict() for doc in logs_ref.stream()]
    except Exception as e:
        print(f"[ERROR] get_log_history(): {str(e)}")
        return []
