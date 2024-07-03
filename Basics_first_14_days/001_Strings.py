# # ------------------------------------------------ Strings
# course = "Python's course for Beginners"
# text = '''
#   Long text ...
#   Extra line
# '''
#
# print("Hello world!\nHello world!\nHello world!")
#
# # ------------------------------------------------ Concatenation
# print("Hello world!" + " " + "Hello Python!")
#
# # ------------------------------------------------ String as char array
# print(course[0])  # 'P' String - array of chars
# print(course[-6])  # 'i' String - array of chars
# print(course[0:4])  # 'Pyth' String - array of chars
# print(course[9:])  # 'course for beginners' String - array of chars
# print(course[:-15])  # 'Python's cours' String - array of chars
# print(course[:])  # 'Python's course for beginners' String - array of chars
# print(course[::-1])  # reversed String
#
# # ------------------------------------------------ slice
# text = "0123456789"
# sl = slice(1, 5, 1) # (from, to, step)
# print(text[sl])  # "1234"
#
# # ------------------------------------------------ Formatted strings
# first = "John"
# last = "Smith"
#
# msg = f'{first} [{last}] is a programmer'  # Formatted string
#
# print(msg)
#
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find('P'))  # return index in string
# print(course.find('Beginners'))  # return first letter index
# print(course.replace('Beginners', 'Winners'))  # Case-sensitive 'Python's course for Winners'
# print('Python' in course)  # True
#
# are = input("What are you? ")  # input - always return string
# print(are)
# course.title()
# course.find()  # course.find(text, char_to_find)
# course.replace()
# course.capitalize()
# print('course' in course)  # True if 'course' in course
#
# # ------------------------------------------------ Split string
# string = "Hello world Python here"
# print(string.split(" "))
#
# # ------------------------------------------------ Concatenation
# text = "Gaius Julius Caesar"
# greeting = "Hi, " + text + "!"  #  Here we use concatenation
#
# age = 24
# name = "John"
# message = "Hi! My name is " + name + ". I'm " + age  # Error
#
# # ------------------------------------------------ Interpolation
# message = f"Hi! My name is {name}. I'm {age}."
# print(message)  # Hi! My name is John. I'm 24.
#
# # ------------------------------------------------ format
# message = "Hi! My name is {name}. I'm {age}.".format(name=name, age=age)
# print(message)  # Hi! My name is John. I'm 24.
#
# # ------------------------------------------------ startswith & endswith
# text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
#
# print(text.startswith("L"))  # True
# print(text.startswith("l"))  # False
# print(text.startswith("Lo"))  # True
# print(text.startswith("Lorem ipsum"))  # True
# print(text.startswith("Lorem ipsum sit"))  # False
#
# print(text.endswith("t"))  # True
# print(text.endswith("T"))  # False
# print(text.endswith(" elit"))  # True
# print(text.endswith("tile "))  # False
#
# # ------------------------------------------------ index & rindex
# text = "abcdbc"
# word = "bc"
#
# print(text.index(word))  # 1
# print(text.rindex(word))  # 4
# print(text.index("rt"))  # ValueError: substring not found
#
# # ------------------------------------------------ find & rfind
# text = "abcdbc"
# word = "bc"
#
# print(text.find(word))  # 1
# print(text.rfind(word))  # 4
# print(text.find("rt"))  # -1
#
# # --------------- text.index(word, from_index, stop_search_index)
# text = "abababab"
# word = "ab"
#
# print(text.index(word, 3, 6))  # 4
# print(text.rindex(word, 4, 7))  # 4
# print(text.find(word, 2, 3))  # -1
# print(text.rfind(word, 2, 7))  # 4
#
# # ------------------------------------------------ number to string
# n = -123
#
# first_string = str(n)  # ------- recommended
# second_string = "%s" % n
# third_string = f"{n}"
#

# def remove_vowels(document: str) -> str:
#     document = document.replace('a', '')
#     document = document.replace('e', '')
#     document = document.replace('i', '')
#     document = document.replace('o', '')
#     document = document.replace('u', '')
#     document = document.replace('y', '')
#     return document

# def remove_vowels(document: str) -> str:
#     clear = ""
#     document = document.lower()
#     for char in document:
#         if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "y":
#             continue
#         clear += char
#     return clear
#
# print(remove_vowels("I like my boss"))

# def make_abbr(words: str) -> str:
#     if len(words) == 0:
#         return ""
#     words_arr = words.split(" ")
#     abbr = ""
#     for word in words_arr:
#         abbr += word[0]
#     return abbr.upper()
# print(make_abbr(""))

# def decrypt_message(message: str) -> str:
#     egassem = ""
#     for i in range(len(message) - 1, -1, -1):
#         egassem += message[i]
#     return egassem
# print(decrypt_message("0202 ni eb lliw cimednap surivanoroc A"))

# def is_werewolf(target: str) -> bool:
#     target_alphas = ""
#     for char in target:
#         if char.isalpha():
#             target_alphas += char
#     return target_alphas.lower() == target_alphas.lower()[::-1]
# print(is_werewolf("eva, can i see bees in a cave"))

# def happy_birthday() -> None:
#     name = input("What's your name?")
#     print(f"Happy birthday, {name}!")
# happy_birthday()

# def parity_checker() -> None:
#     # write your code here
#     number = int(input("What number do you want to check?"))
#     if number % 2 == 0 or number == 0:
#         print("Even")
#     else:
#         print("Odd")
# parity_checker()

# def get_success_rate(statistics: str) -> int:
#     if statistics == "":
#         return 0
#     students_count = len(statistics)
#     yes = statistics.count("1")
#     res = yes / students_count
#     if res == 1:
#         return 100
#     return round(res * 100)
# print(get_success_rate("111100"))

