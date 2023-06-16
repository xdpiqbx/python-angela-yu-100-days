# import random
#
# #  Print letters from string
# for item in 'Python':
#     print(item)
#
# #  foreach
# for item in ['Python', 'Java', 'JS']:
#     print(item)
#
# for item in [1, 2, 3]:
#     print(item)
#
# # ----------------------------------------------- Range arguments
# from_val = 5
# to_val = 15
# step = 2
#
# for item in range(to_val):
#     print(item)
#
# for item in range(from_val, to_val):
#     print(item)
#
# for item in range(from_val, to_val, step):
#     print(item)
#
# # ----------------------------- reverse
# for i in range(3, 0, -1):
#     print(i)
#
# # ----------------------------------------------- Nested loop
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')
#
# # ----------------------------------------------- Exercise
# print("Exercise")
# # numbers = [5, 2, 5, 2, 2]
# # for num in numbers:
# #     print('x' * num)
#
# numbers = [5, 2, 5, 2, 2]
# for num in numbers:
#     output = ''
#     for count in range(num):
#         output += 'x'
#     print(output)
#
# # ----------------------------------------------- Exercise Average
# student_heights = [180, 124, 165, 173, 189, 169, 146]
# total_height = 0
# count = 0
#
# for height in student_heights:
#     count += 1
#     total_height += height
#
# average = round(total_height / count)
#
# print(average)
#
# # ----------------------------------------------- Exercise Max in Array
# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# print(student_scores)
# max_score = student_scores[0]
# for score in student_scores:
#     if max_score < score:
#         max_score = score
# print(f"The highest score in the class is: {max_score}")
#
# # ----------------------------------------------- Exercise sum of all the even numbers
# even_sum = 0;
# for i in range(0, 101, 2):  # from_val, to_val, step
#     even_sum += i
# print(even_sum)
#
# # ----------------------------------------------- Exercise FizzBuzz
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
#
# # ----------------------------------------------- Exercise Password generator
# # Password Generator Project
#
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
#
# password = []
#
# for i in range(nr_letters):
#     password.append(random.choice(letters))
#
# for i in range(nr_numbers):
#     password.append(random.choice(numbers))
#
# for i in range(nr_symbols):
#     password.append(random.choice(symbols))
#
# random.shuffle(password)
#
# res_pass = ""
# for letter in password:
#     res_pass += letter
#
# print(res_pass)
#
# # ----------------------------------------------- Summary Methods
#
# # len()
# # sum()  # Sum elements in list
# # round()
# # max()  # return max num from array
# # min()  # return min num from array
# # list()  # convert string to list of chars
# # random.shuffle(some_list)
# # random.choice(symbols)
#
import math


# def print_numbers(n: int) -> None:
#     for i in range(n):
#         print(i)
# print_numbers(3)

# def get_drinks(number_of_guests: int) -> int:
#     # write your code here
#     total = 0
#     for i in range(number_of_guests):
#         i += 1
#         total += i
#     return total
# print(get_drinks(5))

# def get_drinks_with_step(number_of_guests: int, step: int) -> int:
#     total = 0
#     for i in range(0, number_of_guests, step):
#         i += 1
#         total += i
#     return total
# print(get_drinks_with_step(5, 3))

# def calculate_profit(amount: int, percent: float | int, period: int) -> int:
#     if amount == 0 or percent == 0 or period == 0:
#         return 0
#     percent /= 100
#     total = 0
#     for _ in range(period):
#         profit = amount * percent
#         amount += profit
#         total += profit
#     return math.floor(total)
# print(calculate_profit(1000, 5.5, 7))









