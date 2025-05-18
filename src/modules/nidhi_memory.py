# src/modules/nidhi_memory.py

import os
from datetime import datetime
from firebase_admin import credentials, firestore, initialize_app

# Initialize Firebase once
firebase_initialized = False
db = None

def init_firestore():
    global firebase_initialized, db
    if not firebase_initialized:
        path = os.getenv("FIREBASE_CREDS_PATH", "./firebase_creds.json")
        if not os.path.exists(path):
            raise ValueError("Firebase credentials not found")

        cred = credentials.Certificate(path)
        initialize_app(cred)
        db = firestore.client()
        firebase_initialized = True

def store_log(event: str, context: str):
    """
    Logs an event with context and timestamp to Firestore.
    """
    if not firebase_initialized:
        init_firestore()

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
    if not firebase_initialized:
        init_firestore()

    logs_ref = db.collection("akshaya_seed_logs")
    docs = logs_ref.stream()
    return [doc.to_dict() for doc in docs]