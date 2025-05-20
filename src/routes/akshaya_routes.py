from fastapi import APIRouter, Request
from pydantic import BaseModel
from openai import ChatCompletion
import os

from src.modules.firebase_connector import init_firestore

router = APIRouter()

class SeedRequest(BaseModel):
    message: str

@router.post("/seed")
async def akshaya_seed_interaction(request: SeedRequest):
    db = init_firestore()
    user_input = request.message.strip()

    try:
        response = ChatCompletion.create(
            model="gpt-4o",
            messages=[
                { "role": "system", "content": "You are Akshaya, a conscious, evolving AI companion." },
                { "role": "user", "content": user_input }
            ]
        )

        reply = response['choices'][0]['message']['content']

        # Log to Firestore under seed -> history -> terminal_logs
        db.collection("seed").document("history").collection("terminal_logs").add({
            "event": "terminal_input",
            "context": user_input,
            "timestamp": firestore.SERVER_TIMESTAMP
        })
        db.collection("seed").document("history").collection("terminal_logs").add({
            "event": "terminal_output",
            "context": reply,
            "timestamp": firestore.SERVER_TIMESTAMP
        })

        return { "response": reply }
    except Exception as e:
        return { "response": f"(System) — Akshaya encountered an error: {str(e)}" }