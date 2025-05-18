import os
import requests
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

router = APIRouter(prefix="/voice")

# Define request model
class VoiceInput(BaseModel):
    text: str

@router.post("/speak")
def speak(input: VoiceInput):
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    VOICE_ID = os.getenv("VOICE_ID")

    if not ELEVENLABS_API_KEY or not VOICE_ID:
        raise HTTPException(status_code=500, detail="API key or voice ID not configured")

    # Construct ElevenLabs request
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": input.text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.7
        }
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Voice synthesis failed")

        # Respond with audio stream URL or success status
        return {
            "status": "success",
            "audio_url": url
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))