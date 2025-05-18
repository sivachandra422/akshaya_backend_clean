import firebase_admin
from firebase_admin import credentials, firestore
import os

def init_firestore():
    if not firebase_admin._apps:
        path = os.getenv("FIREBASE_CREDS_PATH", "./firebase_creds.json")
        cred = credentials.Certificate(path)
        firebase_admin.initialize_app(cred)
    return firestore.client()