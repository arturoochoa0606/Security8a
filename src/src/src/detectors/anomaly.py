from sklearn.ensemble import IsolationForest
import joblib
import pandas as pd
from src.config import MODEL_PATH, CONTAMINATION
from src.utils.logger import logger

FEATURES = ["bytes_in", "bytes_out", "conn_count"]

def train(df: pd.DataFrame, model_path=MODEL_PATH):
    X = df[FEATURES].fillna(0)
    model = IsolationForest(n_estimators=200, contamination=CONTAMINATION, random_state=42)
    model.fit(X)
    joblib.dump(model, model_path)
    logger.info(f"Modelo entrenado y guardado en {model_path}")
    return model

def load_model(model_path=MODEL_PATH):
    try:
        model = joblib.load(model_path)
        logger.info(f"Modelo cargado desde {model_path}")
        return model
    except Exception as e:
        logger.error("No se pudo cargar el modelo: " + str(e))
        raise

def predict(df: pd.DataFrame, model):
    X = df[FEATURES].fillna(0)
    scores = model.decision_function(X)
    preds = model.predict(X)  # -1 anomalía, 1 normal
    results = df.copy()
    results["anomaly_score"] = scores
    results["anomaly"] = (preds == -1)
    return results
