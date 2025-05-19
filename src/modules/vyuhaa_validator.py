# === VYUHA Validator — Structure Sentinel ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

import os

REQUIRED_PATHS = [
    "src/core/akshaya_core.py",
    "src/modules/nidhi_memory.py",
    "src/modules/reflection_oracle.py",
    "src/modules/recursive_patch_engine.py",
    "src/modules/firebase_connector.py",
    "src/modules/vyaktitva_manifestor.py",
    "src/modules/sankalpa_directive_engine.py",
    "src/modules/github_commit_reader.py",
    "src/scheduler/tala_scheduler.py",
    "src/scheduler/scheduler_core.py",
    "src/utils/env_loader.py",
    "src/utils/log_formatter.py"
]

def validate_structure(base_path=".") -> dict:
    missing = []
    for rel_path in REQUIRED_PATHS:
        full_path = os.path.join(base_path, rel_path)
        if not os.path.isfile(full_path):
            missing.append(rel_path)

    return {
        "status": "ok" if not missing else "incomplete",
        "missing": missing,
        "checked": len(REQUIRED_PATHS)
    }
