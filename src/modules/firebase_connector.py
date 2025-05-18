import os
import json
from dotenv import load_dotenv
from firebase_admin import credentials

load_dotenv()  # Will load .env only when it exists

firebase_creds_raw = os.getenv("FIREBASE_CREDS_JSON")

# For local dev fallback to file if ENV is missing
if not firebase_creds_raw and os.path.exists("./firebase_creds.json"):
    with open("./firebase_creds.json") as f:
        firebase_creds_raw = f.read()

if not firebase_creds_raw:
    raise ValueError("Firebase credentials not found")

firebase_creds_dict = json.loads(firebase_creds_raw)
cred = credentials.Certificate(firebase_creds_dict)