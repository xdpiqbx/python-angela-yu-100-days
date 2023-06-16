def combine_lists(ls1: list, ls2: list) -> list:
    size = len(ls1)
    if size == 0:
        return []
    result = []
    for i in range(size):
        result.append(ls1[i] + ls2[i])
    return result



combine_lists([1, 2, 5], [3, 6, 1])  # [4, 8, 6]
combine_lists([1], [6])  # [7]
combine_lists([], [])  # []