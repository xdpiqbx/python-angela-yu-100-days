import random

random_integer = random.randint(5, 20)  # rand between 5 - 20
random_float = random.random()  # rand from 0 to 1

# ------------------------------------------- "Heads" or "Tails"

print("Heads") if random.randint(0, 1) == 1 else print("Tails")

# ------------------------------------------- "Red" or "Black"
loose = 0
for x in range(1000):
    count = 0
    balance = 10000000
    isWin = False
    bet = 1
    balance -= bet
    Loose = False
    while count != 1000:
        # print(f"Count:{count} isWin:{isWin} balance:{balance} bet:{bet}")
        if random.randint(0, 1) == 1:
            isWin = True
        else:
            isWin = False

        if isWin:
            balance += bet * 2
            bet = 1
            balance -= bet
        else:
            bet *= 2
            balance -= bet
            if balance < 0:
                loose += 1
                break
        count += 1
    # print(f"Count:{count} balance:{balance} bet:{bet}")
print(loose)

# ----------------------------------------------- Summary Methods

# random.shuffle(some_list)
# range()