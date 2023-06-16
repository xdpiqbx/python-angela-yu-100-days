def get_lists_sum(ls1: list, ls2: list) -> int:
    ls1.extend(ls2)
    total = 0
    for num in ls1:
        total += num
    return total

get_lists_sum([1, 2], [3, 4])  # 1 + 2 + 3 + 4 = 10
get_lists_sum([1, 2, 3, 4], [5, 6, 7, 8])  # 36
get_lists_sum([], [])  # 0