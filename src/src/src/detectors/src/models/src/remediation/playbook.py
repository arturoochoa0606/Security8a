"""
Playbook de remediación seguro y controlado.
Las acciones son simuladas: se registran, se crean tickets y se requiere aprobación humana
para cualquier acción que afecte la red o servicios.
"""
from dataclasses import dataclass
from datetime import datetime
from src.utils.logger import logger
import uuid
import json
from pathlib import Path
from src.config import BASE_DIR

TICKETS_DIR = BASE_DIR / "tickets"
TICKETS_DIR.mkdir(parents=True, exist_ok=True)

@dataclass
class Ticket:
    id: str
    created_at: str
    src_ip: str
    dst_ip: str
    reason: str
    severity: str
    status: str

def create_ticket(src_ip: str, dst_ip: str, reason: str, severity: str = "medium") -> Ticket:
    t = Ticket(
        id=str(uuid.uuid4()),
        created_at=datetime.utcnow().isoformat(),
        src_ip=src_ip,
        dst_ip=dst_ip,
        reason=reason,
        severity=severity,
        status="open"
    )
    path = TICKETS_DIR / f"{t.id}.json"
    with open(path, "w") as f:
        json.dump(t.__dict__, f, indent=2)
    logger.info(f"Ticket creado {t.id} para {src_ip} -> {dst_ip}: {reason}")
    return t

def simulate_isolate_host(ip: str, reason: str):
    """
    Simulación de aislamiento: registra la intención y crea un ticket.
    NO ejecuta comandos de red ni modifica infraestructura.
    """
    logger.warning(f"[SIMULACIÓN] Aislamiento solicitado para {ip}: {reason}")
    t = create_ticket(src_ip=ip, dst_ip="", reason=f"Aislamiento simulado: {reason}", severity="high")
    return t
