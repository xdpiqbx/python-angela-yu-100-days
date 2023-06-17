def sum_list_items(ls: list) -> int:
    sum = 0
    for num in ls:
        sum += num
    return sum

print(sum_list_items([1, 2, 3, 4, 5]) == 15)