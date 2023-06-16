def is_tidy(number: int) -> bool:
    str_numbers = str(number)
    return all(
            int(str_numbers[i]) <= int(str_numbers[i + 1])
            for i in range(len(str_numbers) - 1)
    )

# Цифри розташовані за зростанням
is_tidy(12)  # True

# Цифри розташовані за спаданням
is_tidy(32)  # False

# 1 > 0
is_tidy(1024)  # False

# Однакові цифри можуть бути поруч
is_tidy(3445)  # True

# Цифри розташовані за зростанням
is_tidy(13579)  # True