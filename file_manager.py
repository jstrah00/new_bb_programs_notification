import os
from logger import get_logger

LAST_PROGRAM_FILE = "/mnt/k3s-volumes/new_bb_programs_notification/last_program.txt"
logger = get_logger(__name__)

def get_saved_last_program():
    logger.debug("Getting saved last program")
    try:
        if not os.path.exists(LAST_PROGRAM_FILE):
            logger.info("Last program file does not exist. Returning empty string.")
            return ""
        with open(LAST_PROGRAM_FILE, "r") as f:
            return f.read()
    except Exception as e:
        logger.error(f"Failed to read last program: {e}")
        return ""

def save_last_program(program):
    logger.debug("Saving last program")
    try:
        os.makedirs(os.path.dirname(LAST_PROGRAM_FILE), exist_ok=True)
        with open(LAST_PROGRAM_FILE, "w") as f:
            f.write(program)
    except Exception as e:
        logger.error(f"Failed to save last program: {e}")
