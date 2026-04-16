"""
Ingestor de logs sintéticos. En entorno real, aquí se conectarían SIEM, syslog, cloud logs.
Este script puede generar un CSV de ejemplo para pruebas.
"""
import argparse
import pandas as pd
import numpy as np
from pathlib import Path
from src.config import DATA_DIR
from src.utils.logger import logger

DATA_DIR.mkdir(parents=True, exist_ok=True)

def generate_synthetic(path: Path, n=5000, seed=42):
    rng = np.random.default_rng(seed)
    # columnas de ejemplo: timestamp, src_ip, dst_ip, bytes_in, bytes_out, conn_count
    timestamps = pd.date_range("2025-01-01", periods=n, freq="T")
    bytes_in = rng.normal(500, 200, size=n).clip(0)
    bytes_out = rng.normal(400, 150, size=n).clip(0)
    conn_count = rng.poisson(2, size=n)
    src_ip = ["10.0.0." + str(i%255) for i in range(n)]
    dst_ip = ["192.168.1." + str((i*3)%255) for i in range(n)]
    df = pd.DataFrame({
        "timestamp": timestamps,
        "src_ip": src_ip,
        "dst_ip": dst_ip,
        "bytes_in": bytes_in.astype(int),
        "bytes_out": bytes_out.astype(int),
        "conn_count": conn_count
    })
    # insertar anomalías sintéticas
    for i in range(0, n, 1000):
        df.loc[i:i+5, ["bytes_in","bytes_out","conn_count"]] = [10000, 12000, 200]
    df.to_csv(path, index=False)
    logger.info(f"Datos sintéticos generados en {path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--generate", action="store_true")
    parser.add_argument("--out", default=str(DATA_DIR / "synthetic_logs.csv"))
    args = parser.parse_args()
    if args.generate:
        generate_synthetic(Path(args.out))
