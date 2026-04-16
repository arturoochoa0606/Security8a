from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from src.detectors.anomaly import load_model, predict
from src.utils.logger import logger
from src.remediation.playbook import create_ticket, simulate_isolate_host
import pandas as pd
from src.config import DATA_DIR

router = APIRouter()

class IngestRequest(BaseModel):
    rows: List[dict]

@router.post("/ingest")
def ingest_logs(payload: IngestRequest):
    df = pd.DataFrame(payload.rows)
    # Guardar temporalmente para análisis
    path = DATA_DIR / "ingested_temp.csv"
    df.to_csv(path, index=False)
    logger.info(f"Ingestados {len(df)} registros")
    return {"status":"ok", "ingested": len(df)}

@router.get("/detect")
def detect_from_sample():
    # Cargar datos sintéticos para demo
    path = DATA_DIR / "synthetic_logs.csv"
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Datos sintéticos no encontrados. Genera con collector.py")
    model = load_model()
    results = predict(df, model)
    # devolver solo top anomalías
    anomalies = results[results["anomaly"]].sort_values("anomaly_score").head(50)
    return {"anomalies_count": int(anomalies.shape[0]), "sample": anomalies.head(10).to_dict(orient="records")}

class RemediateRequest(BaseModel):
    src_ip: str
    dst_ip: str
    reason: str
    action: str  # "ticket" o "isolate_sim"

@router.post("/remediate")
def remediate(req: RemediateRequest):
    if req.action == "ticket":
        t = create_ticket(req.src_ip, req.dst_ip, req.reason, severity="high")
        return {"ticket_id": t.id}
    elif req.action == "isolate_sim":
        t = simulate_isolate_host(req.src_ip, req.reason)
        return {"ticket_id": t.id, "note": "Aislamiento simulado; requiere aprobación humana para acciones reales."}
    else:
        raise HTTPException(status_code=400, detail="Acción no soportada")
