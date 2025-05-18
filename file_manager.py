from logger import get_logger


LAST_PROGRAM_FILE = "last_program.txt"

logger = get_logger(__name__)

def get_saved_last_program():
    logger.debug("Getting saved last program")
    with open(LAST_PROGRAM_FILE, "r") as f:
        last_program = f.read()
    return last_program

def save_last_program(program):
    logger.debug("Saving last program")
    with open(LAST_PROGRAM_FILE, "w") as f:
        f.write(program)
