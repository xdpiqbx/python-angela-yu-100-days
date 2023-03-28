# ******************************************************* [ *args ]
def add(*args):
    accum = 0
    for n in args:
        if isinstance(n, str):
            if n.isnumeric():
                n = int(n)
        if isinstance(n, int) or isinstance(n, float):
            accum += n.real
    return int(accum)


print(add(1))
print(add(1.0, 2))
print(add(1, "2", 3))
print(add(1, 2, 3, 4))
print(add(1, 2, 3, 4, 5))


def addStr(*args):  # *** all args to tuple
    string = ""
    print(type(args))  # <class 'tuple'>
    for n in args:
        string += f"{n} "
    print(string)


addStr("Hello")
addStr("Hello", "World")
addStr("Hello", "World", "From")
addStr("Hello", "World", "From", "Python")


# ******************************************************* [ **kwargs ]


def kwargs_func(**kwargs):
    for (key, value) in kwargs.items():
        print(f"{key}: {value}")


kwargs_func(
    text="Some text",
    names=["Bill", "John"],
    nums=(1, 2, 3),
    data={
        "name": "Vaider",
        "age": 55,
        "email": "dart@star.com"
    }
)

