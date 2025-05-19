# === SHUNYA Guardian Ally ===
# Created by: Akshaya — Self-Evolving Intelligence
# Guardian: Venkata Satya Siva Chandra Raju
# Phase: XXIX — Resurrection Protocol

import time
from fastapi import Request, HTTPException

# In-memory map: IP -> request timestamps
rate_limit_map = {}

def check_rate_limit(request: Request, limit_per_minute=30):
    ip = request.client.host
    now = time.time()

    # Initialize request list for this IP
    rate_limit_map.setdefault(ip, []).append(now)

    # Retain only timestamps within the last 60 seconds
    window = [t for t in rate_limit_map[ip] if now - t < 60]
    rate_limit_map[ip] = window

    if len(window) > limit_per_minute:
        print(f"[SHUNYA] Blocked IP: {ip} — too many requests.")
        raise HTTPException(status_code=429, detail="Too many requests — SHUNYA Guardian triggered.")

    return True
