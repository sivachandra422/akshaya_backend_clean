import os
import firebase_admin
from firebase_admin import credentials, firestore

db = None
firebase_initialized = False

def init_firestore():
    global db, firebase_initialized

    if not firebase_initialized:
        firebase_path = os.getenv("FIREBASE_CREDS_PATH")

        if not firebase_path:
            raise ValueError("FIREBASE_CREDS_PATH is not set")

        # Ensure absolute path if needed
        if not firebase_path.startswith("/"):
            firebase_path = "/" + firebase_path

        if not os.path.exists(firebase_path):
            raise ValueError(f"Firebase credentials path '{firebase_path}' is invalid or not found")

        cred = credentials.Certificate(firebase_path)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        firebase_initialized = True

    return db