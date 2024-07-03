# print("Start !!!")
# print('o----')
# print(' ||||')
# print('*' * 10)

# ------------------------------------------------ Types

# Text Type:        str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:     dict
# Set Types:        set, frozenset
# Boolean Type:     bool
# Binary Types:     bytes, bytearray, memoryview
# None Type:        NoneType

# ---- Mutable
# list, dict, set, user-defined-classes

# ---- Immutable
# str, bool, int, float, tuple, NoneType, range ...

# Example                                       Data Type
# x = "Hello World"                             str
# x = 20                                        int
# x = 20.5                                      float
# x = 1j                                        complex
# x = ["apple", "banana", "cherry"]	            list
# x = ("apple", "banana", "cherry")	            tuple
# x = range(6)                                  range
# x = {"name" : "John", "age" : 36}	            dict
# x = {"apple", "banana", "cherry"}	            set
# x = frozenset({"apple", "banana", "cherry"})	frozenset
# x = True                                      bool
# x = b"Hello"                                  bytes
# x = bytearray(5)                              bytearray
# x = memoryview(bytes(5))                      memoryview
# x = None                                      NoneType

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
