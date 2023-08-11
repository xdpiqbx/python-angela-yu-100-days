class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            return function(args[0])
        print("You must login")
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

bill = User('Bill')
bill.is_logged_in = True
create_blog_post(bill)

# ============================================================
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}({args},{kwargs})")
        print(f"It returned: {function(*args, **kwargs)}")
    return wrapper

@logging_decorator
def my_func(a, b, c):
    return sum([a, b, c])

my_func(1, 2, 3)
