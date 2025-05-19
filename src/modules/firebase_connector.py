# === Firebase Connector ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

import os
from google.cloud import firestore
from google.oauth2 import service_account

firebase_initialized = False
db = None

def init_firestore():
    global firebase_initialized, db

    if firebase_initialized and db:
        return db

    try:
        # Updated path variable to match Render secrets
        key_path = os.getenv("FIREBASE_CREDS_CREDENTIALS", "/etc/secrets/firebase_creds.json")
        if not os.path.isfile(key_path):
            raise FileNotFoundError(f"Firebase credentials file not found at: {key_path}")

        credentials = service_account.Credentials.from_service_account_file(key_path)
        db = firestore.Client(credentials=credentials)
        firebase_initialized = True
        print("[FIREBASE] Firestore initialized successfully.")
        return db

    except Exception as e:
        print(f"[FIREBASE] Initialization failed: {str(e)}")
        raise e
