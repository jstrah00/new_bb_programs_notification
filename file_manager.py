LAST_PROGRAM_FILE = "last_program.txt"


def get_saved_last_program():
    with open(LAST_PROGRAM_FILE, "r") as f:
        last_program = f.read()
    return last_program

def save_last_program(program):
    with open(LAST_PROGRAM_FILE, "w") as f:
        f.write(program)
