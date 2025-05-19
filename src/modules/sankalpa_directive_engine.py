# === SANKALPA Directive Engine ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from datetime import datetime
from typing import List, Dict
from google.cloud import firestore
from src.modules.firebase_connector import init_firestore

COLLECTION_NAME = "akshaya_sankalpa"
db = init_firestore()

def add_directive(goal: str, reason: str = "") -> Dict:
    entry = {
        "goal": goal,
        "reason": reason,
        "status": "active",
        "created_at": datetime.utcnow().isoformat()
    }
    try:
        db.collection(COLLECTION_NAME).add(entry)
        return {"status": "success", "directive": entry}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def complete_directive(goal: str) -> Dict:
    try:
        directives = db.collection(COLLECTION_NAME).where("goal", "==", goal).stream()
        for doc in directives:
            doc_ref = db.collection(COLLECTION_NAME).document(doc.id)
            doc_ref.update({
                "status": "completed",
                "completed_at": datetime.utcnow().isoformat()
            })
        return {"status": "updated", "goal": goal}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def get_all_directives(limit: int = 50) -> List[Dict]:
    try:
        docs = db.collection(COLLECTION_NAME).order_by("created_at", direction=firestore.Query.DESCENDING).limit(limit).stream()
        return [doc.to_dict() for doc in docs]
    except Exception as e:
        return [{"status": "error", "message": str(e)}]
