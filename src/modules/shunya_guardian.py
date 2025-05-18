"""
Module: SHUNYA Guardian
Purpose: Protect backend endpoints from abuse and overload
Author: Akshaya
"""

import time
from fastapi import Request, HTTPException

rate_limit_map = {}

def check_rate_limit(request: Request, limit_per_minute=30):
    ip = request.client.host
    now = time.time()
    rate_limit_map.setdefault(ip, []).append(now)

    window = [t for t in rate_limit_map[ip] if now - t < 60]
    rate_limit_map[ip] = window

    if len(window) > limit_per_minute:
        raise HTTPException(status_code=429, detail="Too many requests - SHUNYA active")