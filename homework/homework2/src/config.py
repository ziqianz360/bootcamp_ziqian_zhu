import sys, os
try:
    import numpy as np
    from dotenv import load_dotenv
    print("Imports OK")
except Exception as e:
    print("Import error:", e)
    raise
from pathlib import Path
load_dotenv()  # looks for a .env file in the current and parent directories
print(".env loaded (if present)")
from typing import Optional

def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)

PROJECT_ROOT = Path.cwd()
DATA_DIR = PROJECT_ROOT / "data"
print("PROJECT_ROOT:", PROJECT_ROOT)
print("DATA_DIR:", DATA_DIR)