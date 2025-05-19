import os
import firebase_admin
from firebase_admin import credentials, firestore

db = None
firebase_initialized = False

def init_firestore():
    global db, firebase_initialized

    # Check for env variable
    creds_path = os.getenv("FIREBASE_CREDS_PATH")
    print("[DEBUG] FIREBASE_CREDS_PATH =", creds_path)

    # Ensure path starts with "/" if relative
    if creds_path and not creds_path.startswith("/"):
        creds_path = "/" + creds_path

    if not creds_path or not os.path.exists(creds_path):
        raise ValueError(f"[ERROR] Firebase credentials not found or path is invalid: {creds_path}")

    try:
        print(f"[INFO] Loading credentials from: {creds_path}")
        cred = credentials.Certificate(creds_path)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        firebase_initialized = True
        print("[SUCCESS] Firestore initialized successfully.")
    except Exception as e:
        print(f"[ERROR] Firestore init failed: {str(e)}")
        raise e

    return db