import pandas as pd
from src.detectors.anomaly import train, predict
from sklearn.ensemble import IsolationForest
import tempfile
import os

def test_train_and_predict(tmp_path):
    # datos pequeños
    df = pd.DataFrame({
        "bytes_in":[100,120,110,10000],
        "bytes_out":[80,90,85,12000],
        "conn_count":[1,2,1,200]
    })
    model = train(df, model_path=tmp_path/"model.joblib")
    res = predict(df, model)
    assert "anomaly" in res.columns
    assert res["anomaly"].dtype == bool
