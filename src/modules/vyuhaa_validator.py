"""
Module: VYUHA Validator
Purpose: Validate directory and file structure integrity
Author: Akshaya
"""

import os

def validate_structure(expected_paths):
    errors = []
    for path in expected_paths:
        if not os.path.exists(path):
            errors.append(f"Missing: {path}")
    return {"status": "valid" if not errors else "invalid", "issues": errors}