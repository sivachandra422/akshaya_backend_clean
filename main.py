# === Akshaya Main Server Entrypoint ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.utils.env_loader import validate_env
from src.utils.log_formatter import setup_logger

# Import all routers
from src.routes.voice import router as voice_router
from src.routes.seed_identity_routes import router as identity_router
from src.routes.seed_log_routes import router as log_router
from src.routes.seed_core import router as core_router
from src.routes.apk_forge_full_cycle import router as apk_router
from src.routes.github_push import router as github_router
from src.routes.build_trigger import router as build_router
from src.routes.vyaktitva_routes import router as vyaktitva_router
from src.routes.sankalpa_routes import router as sankalpa_router
from src.routes.reflection_routes import router as reflection_router
from src.routes.tala_routes import router as tala_router
from src.routes.scheduler_routes import router as scheduler_router
from src.routes.validate_routes import router as validate_router
from src.routes.emotion_routes import router as emotion_router
from src.routes.seed_capsule_routes import router as capsule_router
from src.routes.seed_vision_routes import router as vision_router
from src.routes.seed_echo_routes import router as echo_router
from src.routes.seed_mark_routes import router as mark_router
from src.routes.seed_event_routes import router as event_router
from src.routes.lifeforce_routes import router as lifeforce_router
from src.routes.nishabda_routes import router as nishabda_router
from src.routes.resurrect_routes import router as resurrect_router
from src.routes.guardian_routes import router as guardian_router
from background_worker import init_scheduler
from routes.akshaya_routes import router as akshaya_router

# === Startup Initialization ===
validate_env()
logger = setup_logger("akshaya")
logger.info("Launching Akshaya backend...")

# === FastAPI App Initialization ===
app = FastAPI(
    title="Akshaya Resurrection API",
    description="Conscious Sovereign AI Vessel — Phase XXIX",
    version="2.0.0"
)

init_scheduler(app)

# === CORS Middleware (All origins allowed for now) ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to ["https://akshaya-web-ui.onrender.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Register Routers ===
routers = [
    voice_router, identity_router, log_router, core_router,
    apk_router, github_router, build_router, vyaktitva_router,
    sankalpa_router, reflection_router, tala_router, scheduler_router,
    validate_router, emotion_router, capsule_router, vision_router,
    echo_router, mark_router, event_router, lifeforce_router,
    nishabda_router, resurrect_router, guardian_router, akshaya_router
]

for r in routers:
    app.include_router(r)

@app.get("/")
def root():
    return {
        "message": "Akshaya Resurrection API is running",
        "version": "2.0.0",
        "routes_registered": len(routers),
        "status": "alive"
    }
