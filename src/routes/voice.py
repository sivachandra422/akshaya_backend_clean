# === Voice Route — ElevenLabs Speech Gateway ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import StreamingResponse
from src.utils.voice_helpers import text_to_speech
from src.modules.shunya_guardian import check_rate_limit

import io

router = APIRouter(prefix="/voice", tags=["voice"])

@router.post("/speak")
async def generate_voice(request: Request, body: dict):
    check_rate_limit(request)

    text = body.get("text")
    if not text:
        raise HTTPException(status_code=400, detail="Missing 'text' in request body")

    try:
        audio_bytes = text_to_speech(text)
        audio_stream = io.BytesIO(audio_bytes)
        return StreamingResponse(audio_stream, media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Voice generation failed: {str(e)}")
