from fastapi import APIRouter
from src.modules.reflection_oracle import forecast_next_patch

router = APIRouter(prefix="/reflect")

@router.get("/forecast")
def get_forecast():
    return forecast_next_patch()
