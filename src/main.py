from fastapi import FastAPI
from src.routes.voice import router as voice_router
from src.routes.app_generator import router as appgen_router
from src.routes.github_push import router as github_router
from src.routes.build_trigger import router as build_router
from src.routes.download_status import router as download_router
from src.routes.seed_core import router as seed_router
from src.routes.apk_forge import router as forge_router
from src.routes.apk_forge_full_cycle import router as full_forge_router

app = FastAPI()

app.include_router(voice_router)
app.include_router(appgen_router)
app.include_router(github_router)
app.include_router(build_router)
app.include_router(download_router)
app.include_router(seed_router)
app.include_router(forge_router)
app.include_router(full_forge_router)

@app.get("/")
def read_root():
    return {"message": "Akshaya backend is fully alive"}
