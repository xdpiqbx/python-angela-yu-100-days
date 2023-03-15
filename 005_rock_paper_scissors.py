import random

rock = '''
    ______
---'   ___)
      (____)
      (____)
      (___)
---.__(__)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)_________
          ___________)
       _______________)
      (____)
---.__(___)
'''

images_rsp = [rock, scissors, paper]

player_select = ""
while player_select != "Q":

    ai_selected = random.randint(0, 2)
    player_select = input("Choose! [0 for Rock] [1 for Scissors] or [2 for Paper]: ")
    result = ""

    try:
        player_select = int(player_select)
    except ValueError:
        if player_select != "Q":
            print("Wrong data")
            continue
        else:
            print("Close game session...")
            print("Stop gaming server...")
            print("Close all connections...")
            print("Nice play. Good Bye!")
    else:
        if ai_selected == player_select:
            result = "Draw =)"
        else:
            if (ai_selected == 0 and player_select == 1)\
                    or (ai_selected == 1 and player_select == 2)\
                    or (ai_selected == 2 and player_select == 0):
                result = "You lose"
            else:
                result = "You Win"

        if 0 <= player_select <= 2:
            print("Player choose:")
            print(images_rsp[player_select])
            print("AI choose:")
            print(images_rsp[ai_selected])
            print(result)
        else:
            print("Wrong data")
