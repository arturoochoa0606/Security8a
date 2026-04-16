# Diagrama de despliegue - Software Security8a

Este diagrama muestra cómo se despliega Security8a en un entorno seguro, encapsulado en Docker y con auditoría institucional.

```mermaid
flowchart LR
    subgraph Lab["Entorno de laboratorio seguro"]
        A[Logs de red / host] --> B[Collector.py]
        B --> C[Modelo IA\nIsolation Forest]
        C --> D[API FastAPI\nendpoints.py]
    end

    subgraph Docker["Contenedor Docker"]
        D --> E[Uvicorn Server]
        E --> F[Puerto 8000 expuesto]
    end

    subgraph Infra["Infraestructura interna"]
        F --> G[SIEM / Red interna]
        F --> H[Dashboard de monitoreo]
    end

    subgraph Auditoría["Auditoría y Control"]
        D --> I[Logger.py\nlogs/]
        D --> J[Playbook.py\ntickets/]
    end

