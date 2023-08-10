def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate(calc_function, a, b):
    return calc_function(a, b)

print(calculate(multiply, 7, 8))
# ==========================================================
def outer_functon():
    print("I'm outer")
    def nested_functon():
        print("I'm inner")
    nested_functon()

outer_functon()
# Output:
    # I'm outer
    # I'm inner
# ==========================================================
def outer_functon():
    print("I'm outer")
    def nested_functon():
        print("I'm inner")
    return nested_functon

inner_function = outer_functon()
inner_function()
# Output:
    # I'm outer
    # I'm inner
# ========================================================== Decorator
from time import sleep, time
def delay_decorator_function(any_function):
    def wrapper_function():
        sleep(2)
        # Do something before, like sleep(..)
        any_function()
        # any_function() Also you can run it twice (if you need)
        # Do something after.
    return wrapper_function

@delay_decorator_function
def say_hello():
    # sleep(2)
    print("Hello")

@delay_decorator_function
def say_bye():
    # sleep(2)
    print("Bye")

@delay_decorator_function
def say_greeting():
    # sleep(2)
    print("How are you?")

# say_hello()  # same as -> delay_decorator_function(say_hello)()

# ========================================================== Decorator with params: Excercise
current_time = time()
print(current_time)
def speed_calc_decorator(curr_time):
    def decorator(function):
        def wrapper():
            start = curr_time
            function()
            end = time()
            print(f"{function.__name__} run speed: {end - start}")
        return wrapper
    return decorator

@speed_calc_decorator(current_time)
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator(current_time)
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()