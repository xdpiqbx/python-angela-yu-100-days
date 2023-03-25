# if elif else
# and or not
# > < == <= >= !=

is_hot = False
is_cold = True

if is_hot:
    print("Drink water")
    print("Hot now")
elif is_cold:
    print("It's cold now")
else:
    print("Enjoy your day")

# =========== Example 1 =========== # if elif else
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"Down payment: ${down_payment}")

# =========== Example 2 =========== # and or
has_high_income = True
has_good_credit = True
has_criminal_record = False

if (has_high_income or has_good_credit) and not has_criminal_record:
    print("Eligible for loan")

# =========== Example 3 =========== # > < == <= >= !=
temperature = 33
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# =========== Example 4 ===========
name = 'John'
if len(name) < 3:
    print("to short")
elif len(name) > 50:
    print("to long")
else:
    print("OK!")

# ------------------------------------------- Ternary Operator
# [on_true] if [expression] else [on_false]
number = 4
print("This is an even number.") if number % 2 == 0 else print("This is an odd number.")

# ------------------------------------------- Exercise BMI
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(int(weight) / (float(height) * float(height)))
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

# ------------------------------------------- Exercise Leap year
year = float(input("Which year you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

# ------------------------------------------- Exercise Pizza
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

bill = 0
if size == 'S':
    bill = 15
    bill += 2 if add_pepperoni == "Y" else 0
elif size == "M":
    bill = 20
    bill += 3 if add_pepperoni == "Y" else 0
elif size == "L":
    bill = 25
    bill += 3 if add_pepperoni == "Y" else 0
bill += 1 if extra_cheese == "Y" else 0
print(f'Your final bill is: ${bill}.')

# ------------------------------------------- Exercise TRUE LOVE

print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

name1 = "Brad Pitt"
name2 = "Jennifer Aniston"

string = (name1 + name2).lower()

true = 0
love = 0

true += string.count("t")
true += string.count("r")
true += string.count("u")
true += string.count("e")

love += string.count("l")
love += string.count("o")
love += string.count("v")
love += string.count("e")

result = int(str(true) + str(love))

if result < 10 or result > 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif 40 <= result <= 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")

# ------------------------------------------- Exercise Treasure Island

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left = (input("Left or Right?").lower() != "right")
if not left:
    print("Wrong turn. Game Over")
else:
    wait = (input("Swim or Wait?").lower() != "swim")
    if not wait:
        print("Better to wait. Game Over")
    else:
        door_yellow = (input("Which door? [red, blue, yellow]").lower() == "yellow")
        if not door_yellow:
            print("Wrong door. Game Over")
        else:
            print("You Win!")
