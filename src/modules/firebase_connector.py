import os
import firebase_admin
from firebase_admin import credentials, firestore

db = None
firebase_initialized = False

def init_firestore():
    global db, firebase_initialized

    if not firebase_initialized:
        # Read the path from environment variable
        firebase_path = os.getenv("FIREBASE_PATH")

        if not firebase_path or not os.path.exists(firebase_path):
            raise ValueError("Firebase credentials not found or path is invalid")

        cred = credentials.Certificate(firebase_path)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        firebase_initialized = True

    return db