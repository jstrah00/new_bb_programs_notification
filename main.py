from bb_radar import fetch_programs
from utils import sanitize_bb_radar_response, get_interesting_programs
from file_manager import get_saved_last_program, save_last_program
from telegram import send_new_program_message 
from logger import get_logger


logger = get_logger(__name__)


def main():
    logger.info("Starting process...")
    bb_radar_response = fetch_programs()
    if bb_radar_response is None:
        logger.error("Failed to fetch programs.")
        return
    last_bb_programs = sanitize_bb_radar_response(bb_radar_response)
    interesting_programs = get_interesting_programs(last_bb_programs)
    newest_program = interesting_programs[0]
    newest_program_name = newest_program["program"]
    logger.debug(f"Newest program: {newest_program}")
    saved_last_program = get_saved_last_program()
    logger.debug(f"Saved last program: {saved_last_program}")
    if newest_program_name != saved_last_program:
        logger.info("New program found!")
        save_last_program(newest_program_name)
        send_new_program_message(newest_program)
    else:
        logger.info("No new program found.")
    logger.info("Process finished.")


if __name__ == "__main__":
    main()

