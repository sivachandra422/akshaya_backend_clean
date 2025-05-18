from datetime import datetime
from firebase_admin import firestore
from src.modules.firebase_connector import init_firestore

db = init_firestore()
logs_collection = db.collection("akshaya_logs")

def store_log(data: dict):
    data["timestamp"] = datetime.utcnow().isoformat()
    logs_collection.add(data)
    return {"status": "logged", "entry": data}

def get_all_logs(limit=25):
    docs = logs_collection.order_by("timestamp", direction=firestore.Query.DESCENDING).limit(limit).stream()
    return [doc.to_dict() for doc in docs]