# ------------------------------------------------ Strings
course = "Python's course for Beginners"
text = '''
  Long text ...
  Extra line
'''

print("Hello world!\nHello world!\nHello world!")

# ------------------------------------------------ Concatenation
print("Hello world!" + " " + "Hello Python!")

# ------------------------------------------------ String as char array
print(course[0])  # 'P' String - array of chars
print(course[-6])  # 'i' String - array of chars
print(course[0:4])  # 'Pyth' String - array of chars
print(course[9:])  # 'course for beginners' String - array of chars
print(course[:-15])  # 'Python's cours' String - array of chars
print(course[:])  # 'Python's course for beginners' String - array of chars

# ------------------------------------------------ Formatted strings
first = "John"
last = "Smith"

msg = f'{first} [{last}] is a programmer'  # Formatted string

print(msg)

print(len(course))
print(course.upper())
print(course.lower())
print(course.find('P'))  # return index in string
print(course.find('Beginners'))  # return first letter index
print(course.replace('Beginners', 'Winners'))  # Case-sensitive 'Python's course for Winners'
print('Python' in course)  # True

are = input("What are you? ")
print(are)
len(course)
course.upper()
course.lower()
course.title()
course.find()
course.replace()
course.capitalize()
print('course' in course)  # True if 'course' in course

# ------------------------------------------------ Split string
string = "Hello world Python here"
print(string.split(" "))
