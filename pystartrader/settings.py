from pathlib import Path
import logging

# System settings
ROOT_DIR = Path(__file__).resolve().parent.parent
GAME_DIR = ROOT_DIR

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%D-%T",
                    filename="file.log",
                    )

GAME_DB = GAME_DIR / "trader.db"

# Game settings
STAR_NAMES = [
    "SOL", "YORK", "BOYD", "IVAN", "REEF", "HOOK", "STAN", "TASK", "SINK",
    "SAND", "QUIN", "GAOL", "KIRK", "KRIS", "FATE"
]
