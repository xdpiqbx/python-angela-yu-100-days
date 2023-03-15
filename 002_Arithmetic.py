# +
# -
# *
# /
# // - always return integer
# % - module
# ** - pow
# += -= *= ....

import math  # https://docs.python.org/3/library/math.html

x = 2.9
print(round(x))  # 3
print(abs(-2.9))  # 2.9

math.ceil(x)  # 3
math.floor(x)  # 2

# ------------------------------------------------ Task

# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number.
# You might have to do some Googling to solve this.💪

print("Welcom to the tip calculator")
bill = float(input("What was hte total bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12 ok 15? "))
people_to_split = int(input("How many people to split the bill? "))

percentage = (percentage / 100) + 1
result = round(((bill / people_to_split) * percentage), 2)

strTipFormatted = "{:.2f}".format((bill / people_to_split) * percentage)

print(f"Each person should pay: {result}")
