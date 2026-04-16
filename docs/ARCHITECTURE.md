# Arquitectura de Software Security8a

Este documento describe la arquitectura modular del sistema de ciberseguridad defensiva con IA.

---

## 📂 Módulos principales

1. **Ingestión (`src/ingest/collector.py`)**
   - Recoge logs de red/host.
   - Genera datos sintéticos para pruebas.
   - Normaliza y guarda en `data/`.

2. **Detección (`src/detectors/anomaly.py`)**
   - Entrena modelos de anomalía (Isolation Forest).
   - Predice registros sospechosos.
   - Devuelve puntuaciones y etiquetas de anomalía.

3. **Modelos (`src/models/train.py`)**
   - Orquesta el entrenamiento con datos de `data/`.
   - Guarda modelos en `models/`.

4. **Remediación (`src/remediation/playbook.py`)**
   - Define playbooks seguros.
   - Crea tickets JSON en `tickets/`.
   - Simula aislamiento de hosts (requiere aprobación humana).

5. **API (`src/api/endpoints.py`)**
   - Endpoints REST con FastAPI.
   - `/ingest`: carga registros.
   - `/detect`: ejecuta detección sobre datos.
   - `/remediate`: genera tickets o simula aislamiento.

6. **Utilidades (`src/utils/logger.py`)**
   - Logging centralizado en archivo y consola.
   - Auditoría de todas las acciones.

7. **Core (`src/main.py`)**
   - Inicializa FastAPI.
   - Registra routers de API.
   - Punto de entrada del servicio.

---

## 🔄 Flujo de datos

```text
[Logs de red/host] 
        ↓
   Ingestión (collector)
        ↓
   DataFrame normalizado
        ↓
   Detector de anomalías (Isolation Forest)
        ↓
   Resultados con scores y etiquetas
        ↓
   API /detect → devuelve anomalías
        ↓
   API /remediate → crea tickets / simula aislamiento
        ↓
   Auditoría en logs + tickets JSON
