import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"
LOGS_DIR = BASE_DIR / "logs"

# Model params
MODEL_PATH = MODELS_DIR / "isolation_forest.joblib"
CONTAMINATION = float(os.getenv("CONTAMINATION", "0.01"))
