import os
import json
from dotenv import load_dotenv
from firebase_admin import credentials

load_dotenv()  # Will load .env only when it exists

def init_firestore():
    path = os.getenv("FIREBASE_CREDS_PATH", "/etc/secrets/firebase_creds.json")
    if not os.path.exists(path):
        raise ValueError("Firebase credentials not found")

    cred = credentials.Certificate(path)
    if not firebase_admin._apps:
        initialize_app(cred)
    return firestore.client()