from fastapi import FastAPI
from src.api.endpoints import router
from src.utils.logger import logger

app = FastAPI(title="Security8a - API defensiva")
app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"service":"security8a", "status":"running"}
