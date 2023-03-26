STARTING_LETTER = "./Input/Letters/starting_letter.txt"
FILE_WITH_NAMES = "./Input/Names/invited_names.txt"


def get_starting_letter():
    with open(STARTING_LETTER) as letter:
        content = letter.read()
        return content


def get_names_and_write_them_to_letters():
    with open(FILE_WITH_NAMES) as names:
        while True:
            name = names.readline()
            if not name:
                break
            create_letter(name.strip())


starting_letter = get_starting_letter()


def create_letter(name):
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as letter:
        letter.write(starting_letter.replace("[name]", name))


get_names_and_write_them_to_letters()
