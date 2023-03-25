count1 = "GLOBAL SCOPE"


def foo():
    count1 = "In FOO"
    print(count1)


foo()  # In FOO
print(count1)  # GLOBAL SCOPE

# --------------------------------------- Change Global variable using 'global' keyword
count2 = "GLOBAL SCOPE"


def foo():
    global count2
    count2 = "In FOO"
    print(count2)


foo()  # In FOO
print(count2)  # In FOO


# --------- Constants. Use a strong naming convention
# Constants are usually defined on a module level and written in all capital letters with underscores separating words.
# Examples:
PI = 3.14
MAX_SPEED = 300
DEFAULT_COLOR = "RGB"
WIDTH = 20
API_TOKEN = "123"
