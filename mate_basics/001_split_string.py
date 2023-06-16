# Реалізуй функцію split_string, яка приймає рядок string,
# ділить його на частини по 2 символи, а потім повертає список з отриманих частин.
#
# Зверни увагу: якщо рядок містить непарну кількість символів, додай символ _ після останнього символу.
#
# Наприклад:
#     split_string("123456")  # ["12", "34", "56"]
#     split_string("ab cd ef")  # ["ab", " c", "d ", "ef"]
#     split_string("abc")  # ["ab", "c_"]
#     split_string(" ")  # [" _"]
#     split_string("")  # []


def split_string(string: str) -> list:
    if len(string) % 2 != 0:
        string += "_"

    list_of_parts = []
    part_of_string = ""

    for char in string:
        part_of_string += char
        if len(part_of_string) == 2:
            list_of_parts.append(part_of_string)
            part_of_string = ""

    print(list_of_parts)

    return list_of_parts

split_string("123456")  # ["12", "34", "56"]
split_string("ab cd ef")  # ["ab", " c", "d ", "ef"]
split_string("abc")  # ["ab", "c_"]
split_string(" ")  # [" _"]
split_string("")  # []
