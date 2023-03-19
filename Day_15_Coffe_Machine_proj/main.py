from data import MENU, resources, coins, short

money_in_coffe_machine = 0
secret = "secret"


def ask_for_action():
    actions = ['E', 'L', 'C', 'report', 'off'+secret]
    action = input("What would you like? (espresso 'E'/latte 'L'/cappuccino 'C'): ")
    if action in actions:
        return action
    return ask_for_action()


def print_report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${money_in_coffe_machine}')


def prepare_coffe(action):
    if is_enough_resources(action):
        if did_paid(action):
            use_resources(action)


def is_enough_resources(action):
    ingredients = MENU[short[action]]["ingredients"]
    ingredient_keys = ingredients.keys()
    for ingredient in ingredient_keys:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def valid_int(message):
    raw_data = input(message)
    if raw_data.isnumeric():
        return int(raw_data)
    return valid_int(message)


def total_coins_calculated():
    quarters = valid_int("How many quarters?")
    dimes = valid_int("How many dimes?")
    nickles = valid_int("How many nickles?")
    pennies = valid_int("How many pennies?")

    return sum([
        coins["quarters"] * quarters,
        coins["dimes"] * dimes,
        coins["nickles"] * nickles,
        coins["pennies"] * pennies,
    ])


def did_paid(action):
    cost = MENU[short[action]]["cost"]
    coffe = short[action].capitalize()

    print(f"{coffe} cost [${cost}]. Please insert coins.")
    coins_sum = total_coins_calculated()

    if coins_sum >= cost:
        if coins_sum > cost:
            print(f"Here is ${round((coins_sum - cost), 2)} in change.")
        print("Here is your ☕ Enjoy!")
        global money_in_coffe_machine
        money_in_coffe_machine += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def use_resources(action):
    ingredients = MENU[short[action]]["ingredients"]
    ingredient_keys = ingredients.keys()
    for ingredient in ingredient_keys:
        resources[ingredient] -= ingredients[ingredient]


def coffe_machine():
    action = ask_for_action()
    if action == 'E':
        prepare_coffe(action)
    elif action == 'L':
        prepare_coffe(action)
    elif action == 'C':
        prepare_coffe(action)
    elif action == 'off'+secret:
        return False
    else:
        print_report()
    return True


is_on = True
while is_on:
    is_on = coffe_machine()
