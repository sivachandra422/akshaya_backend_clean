from fastapi import APIRouter
from src.modules.vyuhaa_validator import validate_structure

router = APIRouter(prefix="/validate")

@router.get("/structure")
def validate_structure_api():
    expected = [
        "src/routes/voice.py",
        "src/routes/app_generator.py",
        "src/routes/github_push.py",
        "src/modules/firebase_connector.py",
        "src/modules/nidhi_memory.py"
    ]
    return validate_structure(expected)