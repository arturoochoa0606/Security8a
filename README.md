# Security8a
ecurity8a es un software de ciberseguridad defensiva con inteligencia artificial, diseñado para detectar anomalías en tráfico y registros internos, predecir intentos de intrusión y activar playbooks de remediación segura. Su enfoque es preventivo y auditado, nunca ofensivo: se centra en proteger la infraestructura,.


**Propósito:** Repositorio de ejemplo para detección de anomalías en logs, priorización de alertas y playbooks de remediación segura.  
**Advertencia legal:** Este proyecto **no** realiza contraataques ni acciones ofensivas. Úsalo solo en entornos controlados y tras revisión legal.

## Estructura
(ver estructura en el repositorio)

## Cómo ejecutar (entorno local)
1. Crear entorno virtual: `python -m venv .venv && source .venv/bin/activate`
2. Instalar dependencias: `pip install -r requirements.txt`
3. Generar datos sintéticos: `python src/ingest/collector.py --generate`
4. Entrenar modelo: `python src/models/train.py`
5. Ejecutar API: `uvicorn src.main:app --reload --port 8000`

## Buenas prácticas
- Ejecutar solo en laboratorio o red de pruebas.
- Revisar `docs/USO_LEGAL.md` antes de desplegar.

                ┌───────────────────────────┐
                │       Ingestión           │
                │   (collector.py, logs)    │
                └─────────────┬─────────────┘
                              │
                              ▼
                ┌───────────────────────────┐
                │       Detección           │
                │   (anomaly.py, modelos)   │
                └─────────────┬─────────────┘
                              │
                              ▼
                ┌───────────────────────────┐
                │       Remediación         │
                │   (playbook.py, tickets)  │
                └─────────────┬─────────────┘
                              │
                              ▼
                ┌───────────────────────────┐
                │           API             │
                │   (endpoints.py, FastAPI) │
                └─────────────┬─────────────┘
                              │
                              ▼
                ┌───────────────────────────┐
                │        Auditoría          │
                │   (logger.py, registros)  │
                └───────────────────────────┘
