
import os
from fastapi import FastAPI
from dotenv import load_dotenv

if os.getenv("RENDER") != "true":
    load_dotenv()

from src.routes.voice import router as voice_router
from src.routes.app_generator import router as appgen_router
from src.routes.github_push import router as github_router
from src.routes.build_trigger import router as build_router
from src.routes.download_status import router as download_router
from src.routes.seed_log_routes import router as seed_log_router
from src.routes.apk_forge_full_cycle import router as apk_forge_router
from src.routes.self_patch_trigger import router as patch_router

from src.scheduler import scheduler

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    scheduler.start()

# Include routers
app.include_router(voice_router)
app.include_router(appgen_router)
app.include_router(github_router)
app.include_router(build_router)
app.include_router(download_router)
app.include_router(seed_log_router)
app.include_router(apk_forge_router)
app.include_router(patch_router)

@app.get("/")
def read_root():
    return {"message": "Akshaya backend with Self-Evolving Core is live"}
