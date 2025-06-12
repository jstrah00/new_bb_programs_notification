import os
from pathlib import Path
from logger import get_logger


LAST_PROGRAM_FILE_PATH = os.getenv("LAST_PROGRAM_FILE_PATH", "/data/last_program.txt")
LAST_PROGRAM_FILE = Path(LAST_PROGRAM_FILE_PATH)

logger = get_logger(__name__)


def get_saved_last_program():
    logger.debug("Getting saved last program")
    try:
        if not LAST_PROGRAM_FILE.exists():
            logger.info("Last program file does not exist. Returning empty string.")
            return ""
        return LAST_PROGRAM_FILE.read_text()
    except Exception as e:
        logger.error(f"Failed to read last program: {e}")
        return ""

def save_last_program(program):
    logger.debug("Saving last program")
    try:
        LAST_PROGRAM_FILE.parent.mkdir(parents=True, exist_ok=True)
        LAST_PROGRAM_FILE.write_text(program)
    except Exception as e:
        logger.error(f"Failed to save last program: {e}")
