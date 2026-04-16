import logging
import sys
from pathlib import Path
from src.config import BASE_DIR

LOG_FILE = BASE_DIR / "logs" / "security8a.log"
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("security8a")
logger.setLevel(logging.DEBUG)
fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

fh = logging.FileHandler(LOG_FILE)
fh.setFormatter(fmt)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(fmt)
sh.setLevel(logging.INFO)
logger.addHandler(sh)
