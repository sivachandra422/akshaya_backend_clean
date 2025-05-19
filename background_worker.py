# === Akshaya Background Scheduler: TĀLA Autonomous Cycle ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXX — Patch Consciousness Engine

import asyncio
import logging
from fastapi import FastAPI
from src.scheduler.tala_scheduler import cycle_status
from src.scheduler.scheduler_core import run_scheduled_cycle
from src.modules.nidhi_memory import insert_log

logger = logging.getLogger("akshaya-tala")

def init_scheduler(app: FastAPI, interval_seconds: int = 21600):  # Default: 6 hours

    @app.on_event("startup")
    async def activate_tala():
        async def cycle_loop():
            while True:
                try:
                    logger.info("[TĀLA] ⏳ Scanning system rhythm...")
                    status = cycle_status()

                    if status.get("due"):
                        logger.info("[TĀLA] ⚡ Patch is due. Executing scheduled cycle...")
                        result = run_scheduled_cycle()

                        insert_log({
                            "event": "tala_patch_cycle",
                            "context": result.get("summary", "Cycle executed."),
                            "timestamp": result.get("timestamp")
                        })

                        logger.info("[TĀLA] ✅ Cycle executed and logged.")
                    else:
                        logger.info("[TĀLA] 🕊 No patch needed right now.")

                except Exception as e:
                    logger.error(f"[TĀLA ERROR] {str(e)}")

                await asyncio.sleep(interval_seconds)

        asyncio.create_task(cycle_loop())
