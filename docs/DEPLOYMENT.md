
```mermaid
flowchart LR
    subgraph Lab["Entorno de laboratorio seguro"]
        A[Logs de red / host] --> B[Collector.py]
        B --> C[Modelo IA<br>(Isolation Forest)]
        C --> D[API FastAPI<br>(endpoints.py)]
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
        D --> I[Logger.py<br>(logs/)]
        D --> J[Playbook.py<br>(tickets/)]
    end
