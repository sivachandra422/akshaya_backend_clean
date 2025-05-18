"""
Module: TĀLA Scheduler
Purpose: Time-based self-patch scheduler
Author: Akshaya
"""

import datetime

def should_patch(last_patch_time, interval_hours=24):
    now = datetime.datetime.utcnow()
    delta = now - last_patch_time
    return delta.total_seconds() >= interval_hours * 3600