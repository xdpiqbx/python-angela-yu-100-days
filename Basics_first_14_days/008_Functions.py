import math


# def greet():
#     print("Hello!!!")


def greet_user(first_name="user", last_name="default"):
    print(f"Hello {first_name} {last_name}!")


greet_user("John", "Smith")
greet_user(last_name="Smith", first_name="John")
# greet_user(last_name="Smith", "John") # Error
greet_user("John")
greet_user()


# ----------------------------------------------- Exercise


# def paint_calc(height, width, cover):
#     cants = math.ceil((height * width) / 5)
#     print(f"You'll need {cants} cans of paint.")
#
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


# ----------------------------------------------- Exercise


# def prime_checker(number):
#     isPrime = True
#     for i in range(2, number):
#         if number % i == 0:
#             isPrime = False
#             print(f"It's not a prime number.")
#             break
#     if isPrime:
#         print(f"It's a prime number.")
#
#
# # Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)


# ----------------------------------------------- Exercise return

# def format_name(f_name, l_name):
#     string = f_name+" "+l_name
#     return string.title()
#
#
# print(format_name("bILLy", "jEnA"))

# ----------------------------------------------- Exercise Leap Year


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    """Input year and month
    this is a docstring"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        month_days[1] += 1
    return month_days[month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

