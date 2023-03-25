import os
import random


from day_Higher_lower_art import logo
from day_Higher_lower_art import vs
from day_Higher_lower_data import data


score = 0
a = random.choice(data)
b = random.choice(data)
while True:
    os.system('cls')
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}")

    a_has_more = a['follower_count'] >= b['follower_count']

    print(f"Compare A: {a['name']}, {a['description']}, {a['country']}")
    print(vs)
    print(f"Against B: {b['name']}, {b['description']}, {b['country']}")

    choice = input("Who has more followers? Type 'A' or 'B': ")

    if (a_has_more and choice == 'A') or (not a_has_more and choice == 'B'):
        score = score + 1
        if a_has_more:
            b = random.choice(data)
        else:
            a = b
            b = random.choice(data)
    else:
        os.system('cls')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break



