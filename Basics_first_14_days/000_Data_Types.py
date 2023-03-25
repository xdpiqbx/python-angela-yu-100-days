# print("Start !!!")
# print('o----')
# print(' ||||')
# print('*' * 10)

# ------------------------------------------------ Variables

# price = 10
# raring = 4.9
# name = 'Artem'
# isValid = True
#
# full_name = input('Name? ')
# print('Hi ' + full_name)

# Large integers and floats write like 123_432_978 instead 123543654

# ------------------------------------------------ Cast type

# int("10")
# float("4.5")
# str("Name")

# type(10) # to check Type

# birth_year = input('Year: ')
# age = 2023 - int(birth_year)
# print(type(age))
# print(age)

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
result = int(weight) / (float(height) * float(height))
print(f"{weight} ÷ ({height} x {height}) = {result}")
print(int(result))