from fastapi import FastAPI
from src.routes.voice import router as voice_router
from src.routes.app_generator import router as appgen_router
from src.routes.github_push import router as github_router
from src.routes.build_trigger import router as build_router
from src.routes.download_status import router as download_router
from src.routes.seed_core import router as seed_router
from src.routes.apk_forge import router as forge_router
from src.routes.apk_forge_full_cycle import router as full_forge_router
from src.routes.ui_injector import router as ui_router
from src.routes.seed_log_routes import router as seed_log_router
from src.routes.self_patch_trigger import router as self_patch_router
from src.routes.reflection_forecast_routes import router as reflection_router
from src.routes.recursive_patch_routes import router as recursive_router
from src.routes.scheduler_routes import router as scheduler_router
from src.routes.seed_expand import router as seed_expand_router
from src.routes.vyuhaa_routes import router as vyuhaa_router

app = FastAPI()

app.include_router(voice_router)
app.include_router(appgen_router)
app.include_router(github_router)
app.include_router(build_router)
app.include_router(download_router)
app.include_router(seed_router)
app.include_router(forge_router)
app.include_router(full_forge_router)
app.include_router(ui_router)
app.include_router(seed_log_router)
app.include_router(self_patch_router)
app.include_router(reflection_router)
app.include_router(recursive_router)
app.include_router(scheduler_router)
app.include_router(seed_expand_router)
app.include_router(vyuhaa_router)

@app.get("/")
def read_root():
    return {"message": "Akshaya backend is fully alive"}
