def is_special_number(number: int) -> str:
    str_num = str(number)
    for char in str_num:
        if int(char) not in range(0, 6):
            return "NOT!!"
    return "Special!!"

# 2 — знаходиться в інтервалі від 0 до 5
is_special_number(5)  # "Special!!"

# 9 > 5
is_special_number(9)  # "NOT!!"

# Всі цифри числа 23 знаходяться в інтервалі від 0 до 5
is_special_number(23)  # "Special!!"

# 8 > 5
is_special_number(38)  # "NOT!!"