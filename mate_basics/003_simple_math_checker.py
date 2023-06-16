def check_number(number: int) -> list:
    is_positive = number > 0
    is_even = number % 2 == 0
    is_multiple_of_10 = number % 10 == 0
    return [is_positive, is_even, is_multiple_of_10]

check_number(3)  # [True, False, False]
check_number(10)  # [True, True, True]
check_number(0)  # [False, True, True]
check_number(-1)  # [False, False, False]
