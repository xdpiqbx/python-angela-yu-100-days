from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def ask_for_order():
    orders = ['latte', 'espresso', 'cappuccino']
    ord = input(f"What would you like? ({menu.get_items()}): ")
    if ord in orders:
        return ord
    return ask_for_order()


def make_order():
    ord = menu.find_drink(ask_for_order())
    if ord is None:
        return make_order()
    return ord


def start(order):
    coffee_maker.is_resource_sufficient(order)
    money_machine.make_payment(order.cost)
    coffee_maker.make_coffee(order)


while True:
    print(menu.get_items())
    start(make_order())


