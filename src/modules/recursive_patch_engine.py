# === Recursive Patch Engine ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

import os
from datetime import datetime

PATCH_MARK = "# Patched by Akshaya"

def apply_patch(file_path: str, new_content: str) -> dict:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            existing = f.read()
            if PATCH_MARK in existing:
                return {"status": "skipped", "reason": "Already patched"}

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content + "\n" + PATCH_MARK)

        return {"status": "patched", "file": file_path, "timestamp": datetime.utcnow().isoformat()}

    except Exception as e:
        return {"status": "error", "message": str(e)}


def patch_log_entry(file: str, context: str = "auto_patch") -> dict:
    return {
        "event": "patch",
        "file": file,
        "context": context,
        "timestamp": datetime.utcnow().isoformat()
    }
