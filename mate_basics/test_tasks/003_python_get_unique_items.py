def get_unique_items(ls: list) -> list:
    filtered_list = []
    [filtered_list.append(num) for num in ls if num not in filtered_list]
    return filtered_list
