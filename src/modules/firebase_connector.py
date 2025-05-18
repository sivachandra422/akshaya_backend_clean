import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

if os.getenv("RENDER") != "true":
    load_dotenv()

def init_firestore():
    path = os.getenv("FIREBASE_CREDS_PATH", "./firebase_creds.json")

    if not os.path.exists(path):
        raise ValueError("Firebase credentials not found")

    if not firebase_admin._apps:
        cred = credentials.Certificate(path)
        firebase_admin.initialize_app(cred)

    return firestore.client()