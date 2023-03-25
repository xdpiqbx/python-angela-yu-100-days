import random

WELLCOME_MESSAGE_1 = "Welcome to the Number Guessing Game!"
WELLCOME_MESSAGE_2 = "I'm thinking of a number between 1 and 100."
CHOOSE_DIFFICULTY = "Choose difficulty. Type easy or hard ('E' / 'H'): "
TOO_HIGH = "Too high."
TOO_LOW = "Too low."
TRY_AGAIN = "Guess again."
HARD = 5
EASY = 10


def attempts_message(count):
    print(f"You have {count} attempts remaining to guess the number")


def winning_message(number):
    print(f"You got it! The answer was {number}.")


def choose_difficulty_level():
    difficulty = input(CHOOSE_DIFFICULTY)
    if difficulty == 'H':
        return HARD
    elif difficulty == 'E':
        return EASY
    else:
        return choose_difficulty_level()


def comparing_numbers(actual, secret):
    if actual > secret:
        print(TOO_HIGH)
        return -1
    elif actual < secret:
        print(TOO_LOW)
        return -1
    elif actual == secret:
        winning_message(secret)
        return 1


def game():
    print(WELLCOME_MESSAGE_1)
    print(WELLCOME_MESSAGE_2)
    secret_number = random.randint(1, 100)

    attempts = choose_difficulty_level()

    while True:
        attempts_message(attempts)
        actual_number = int(input("Make a guess: "))

        if comparing_numbers(actual_number, secret_number) > 0:
            return
        else:
            attempts -= 1

        if attempts == 0:
            print("You have run out of guesses, you lose.")
            return

        print(TRY_AGAIN)


game()



