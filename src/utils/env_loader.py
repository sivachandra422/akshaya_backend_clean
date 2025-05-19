# === ENV Loader & Validator ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

import os

REQUIRED_ENV_VARS = [
    "OPENAI_API_KEY",
    "ELEVENLABS_API_KEY",
    "VOICE_ID",
    "GITHUB_TOKEN",
    "GITHUB_USERNAME",
    "GITHUB_REPO_NAME",
    "FIREBASE_CREDENTIALS"
]

def validate_env():
    missing = [key for key in REQUIRED_ENV_VARS if not os.getenv(key)]
    if missing:
        raise EnvironmentError(f"Missing required environment variables: {', '.join(missing)}")
    return True
