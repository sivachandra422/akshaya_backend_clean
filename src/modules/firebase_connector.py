# src/modules/firebase_connector.py
import os
import firebase_admin
from firebase_admin import credentials, firestore

def init_firestore():
    path = os.getenv("FIREBASE_PATH", "/etc/secrets/firebase_creds.json")

    if not os.path.exists(path):
        raise ValueError(f"Firebase credentials not found at: {path}")

    if not firebase_admin._apps:
        cred = credentials.Certificate(path)
        firebase_admin.initialize_app(cred)

    return firestore.client()