def get_three_largest(ls: list) -> list:
    unic_numbers_list = []
    [unic_numbers_list.append(num) for num in ls if num not in unic_numbers_list]
    unic_numbers_list.sort(reverse=True)
    return unic_numbers_list[:3]

# def get_three_largest(ls: list) -> list:
#     ls.sort(reverse=True)
#     return ls[:3]

print(get_three_largest([100, 10, 101, 100, 15, 6, -10]))
