from bb_radar import fetch_programs
from utils import sanitize_bb_radar_response, get_interesting_programs
from file_manager import get_saved_last_program, save_last_program
from telegram import send_new_program_message 


def main():
    print("Starting process...")
    bb_radar_response = fetch_programs()
    if bb_radar_response is None:
        print("Failed to fetch programs.")
        return
    last_bb_programs = sanitize_bb_radar_response(bb_radar_response)
    interesting_programs = get_interesting_programs(last_bb_programs)
    newest_program = interesting_programs[0]
    newest_program_name = newest_program["program"]
    print("Newest program: ", newest_program)
    saved_last_program = get_saved_last_program()
    print("Saved last program: ", saved_last_program)
    if newest_program_name != saved_last_program:
        print("New program found!")
        save_last_program(newest_program_name)
        print("Saved new program.")
        send_new_program_message(newest_program)
    else:
        print("No new program found.")
    print("Process finished.")


if __name__ == "__main__":
    main()


# TODO:
# - Save newest program
# - Notify if new 'newest' program is found
