import os
import firebase_admin
from firebase_admin import credentials, firestore, get_app, initialize_app
from functools import lru_cache

# === Initialization Log ===
def _log(msg):
    print(f"[Akshaya.Firebase] {msg}")

# === Firebase App Singleton ===
def init_firebase_app():
    if not firebase_admin._apps:
        cred_path = os.getenv("FIREBASE_CREDS_CREDENTIALS", "firebase_creds.json")
        if not os.path.exists(cred_path):
            raise FileNotFoundError(f"Firebase credentials not found at: {cred_path}")
        cred = credentials.Certificate(cred_path)
        initialize_app(cred)
        _log("Firebase initialized with credentials.")
    else:
        _log("Firebase already initialized.")
    return get_app()
    
def get_firestore_client():
    firebase_creds_path = os.getenv("FIREBASE_CREDS_CREDENTIALS", "firebase_creds.json")

    if not firebase_admin._apps:
        cred = credentials.Certificate(firebase_creds_path)
        firebase_admin.initialize_app(cred)

    return firestore.client()

# === Firestore Singleton ===
@lru_cache(maxsize=1)
def init_firestore():
    try:
        init_firebase_app()
        db = firestore.client()
        _log("Firestore client initialized.")
        return db
    except Exception as e:
        _log(f"ERROR: Firestore initialization failed: {e}")
        raise