def is_jumping(number: int) -> str:
    str_numbers = str(number)
    if all(
            int(str_numbers[i]) + 1 == int(str_numbers[i + 1]) or
            int(str_numbers[i]) - 1 == int(str_numbers[i + 1])
            for i in range(len(str_numbers) - 1)
    ):
        return "JUMPING"
    else:
        return "NOT JUMPING"

# Число з однієї цифри
is_jumping(9)  # "JUMPING"

# 7 і 9 відрізняються на 2, а не на 1
is_jumping(79)  # "NOT JUMPING"

# Різниця між однаковими цифрами дорівнює 0
is_jumping(7889)  # "NOT JUMPING"

# Усі сусідні цифри відрізняються на 1
is_jumping(23454)  # "JUMPING"