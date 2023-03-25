from day_Calculator_art import logo


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


calculation = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': div,
}


def calc():
    print(logo)
    symbols_str = ""
    for symbol in calculation.keys():
        symbols_str += symbol + " "
    symbols_str = symbols_str.strip()

    num1 = float(input("Number 1: "))
    while True:
        symbol = input(f"Pick operation from [{symbols_str}]: ")
        num2 = float(input("Next Number: "))
        result = calculation[symbol](num1, num2)
        print(f"{num1} {symbol} {num2} = {result}")
        if input("Type 'y' to continue, 'n' to exit") == 'n':
            calc()
            break
        num1 = result


calc()



