# А тепер ти навчишся змінювати порядок символів у рядку.
#
# Напиши функцію scrolling_text, яка:
#
# - приймає рядок string;
#   послідовно переставляє всі символи в рядку з нульового індексу на останній;
# - повертає список з отриманими комбінаціями рядка у верхньому регістрі.
#
# Наприклад, для слова "robot":
#
# перший крок: беремо першу літеру ("r") слова "robot" і переставляємо її в кінець слова — "obotr";
# другий крок: беремо першу літеру ("о") слова "obotr" і переставляємо її в кінець – "botro" і так далі.
#
# У консолі ми побачимо:
# [ "ROBOT",  # Спочатку вхідне слово
#   "OBOTR",  # Потім із переставленим порядком символів
#   "BOTRO",
#   "OTROB",
#   "TROBO" ]

def scrolling_text(string: str) -> list:
    if len(string) == 0:
        return []
    iterations = len(string) - 1
    upper_str = string.upper()
    list_of_strs = [upper_str]
    for _ in range(iterations):
        upper_str = upper_str[1:] + upper_str[0]
        list_of_strs.append(upper_str)
    return list_of_strs

scrolling_text("robot")