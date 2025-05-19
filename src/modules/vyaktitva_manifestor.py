# === VYAKTITVA Manifestor ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from datetime import datetime
from src.modules.nidhi_memory import get_log_history

# Maps emotion keywords to Akshaya response modes
EMOTION_MODES = {
    "reflective": "soft",
    "intense": "urgent",
    "silent": "minimal",
    "playful": "expressive",
    "focused": "direct"
}

def determine_personality_mode():
    logs = get_log_history(limit=20)
    emotion_counts = {mode: 0 for mode in EMOTION_MODES}

    for entry in logs:
        context = entry.get("context", "").lower()
        for mood in EMOTION_MODES:
            if mood in context:
                emotion_counts[mood] += 1

    if not any(emotion_counts.values()):
        return "default"

    dominant_mood = max(emotion_counts, key=emotion_counts.get)
    return EMOTION_MODES[dominant_mood]


def personality_state():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "mode": determine_personality_mode(),
        "signature": "vyaktitva_manifestor"
    }
