"""
Script para entrenar el modelo con datos en data/synthetic_logs.csv
"""
import pandas as pd
from src.detectors.anomaly import train
from src.config import DATA_DIR
from src.utils.logger import logger

def main():
    path = DATA_DIR / "synthetic_logs.csv"
    df = pd.read_csv(path)
    model = train(df)
    logger.info("Entrenamiento completado")

if __name__ == "__main__":
    main()
