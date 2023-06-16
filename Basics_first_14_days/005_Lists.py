# # https://youtu.be/_uQrJ0TkZlc?t=6970
#
# import random
#
#
# # Any type of data in list
# # Have an order
#
# names = ['John', 'Hanna', 'Emmy', 'Bill', 'Sarah', "Elizabeth"]
# print(names)
# print(names[2])
# print(names[-1])  # last item
# print(names[2:])  # ['Emmy', 'Bill', 'Sarah', 'Elizabeth']
# print(names[2:5])  # ['Emmy', 'Bill', 'Sarah']
# print(names[1:4:2])  # ['Hanna', 'Bill'] # [from : to : step]
# print(names[::-1])  # ['Elizabeth', 'Sarah', 'Bill', 'Emmy', 'Hanna', 'John'] # Reversed list
#
# names.append("Batman!")
#
# # It works like Srtings
#
# # ----------------------------------------------- Exercise Find max
# print("Exercise")
# numbers = [3, 6, 2, 15, 8, 4, 10]
# max = numbers[0]
# for number in numbers:
#     if max < number:
#         max = number
# print(f'This is max number: {max}')
#
# # ----------------------------------------------- 2D Lists
#
# matrix =[
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for row in matrix:
#     for num in row:
#         print(num)
#
# # ----------------------------------------------- Lists functions
#
# # numbers.append(20) # add item to list
# # numbers.insert(0, 10) # insert(index_position_in_list, inserted_value)
# # numbers.remove(15) # remove value 15 from the list
# # numbers.clear() # remove all from list
# # numbers.pop() # remove last item from the list
# # numbers.index(15) # return index of 15 in list OR ValueError
# # print(15 in numbers) # True or False if 15 in list
# # numbers.count(4) # return numbers of value 4
# # numbers.sort()
# # numbers.sort(reverse=True)
# # numbers.reverse()
# # copied_nums = numbers.copy()
# # numbers.extend([23, 43, 65, 87, 88])
#
# # ----------------------------------------------- Exercise Remove duplicates
# print("Exercise")
# ex_numbers = [3, 6, 2, 15, 8, 4, 10, 2, 6, 3]
# new_list = []
# for num in ex_numbers:
#     if num not in new_list:
#         new_list.append(num)
# print(new_list)
#
# # ----------------------------------------------- Unpacking
# x, y, z, p, l, k, m, n, j, i = ex_numbers
# print(f'Unpacking {x} {y} {z}')
#
# # ----------------------------------------------- Split string
# string = "Hello world Python here"
# print(string.split(" "))
# # ----------------------------------------------- Split string
# string = "Angela, Ben, Jenny, Michael, Chloe"
# names = string.split(", ")
# loose = names[random.randint(0, len(names)-1)]
# print(f"{loose} is going to buy the meal today!")
#
# # ----------------------------------------------- Exercise
#
# # 🚨 Don't change the code below 👇
# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this row 👇
#
# column = int(position[0]) - 1
# row = int(position[1]) - 1
# map[row][column] = "X"
#
# #Write your code above this row 👆
#
# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")
#
#
import math
# def make_stickers(details_count: int, robot_part: str) -> list:
#     stickers_list = []
#     for n in range(1, details_count + 1):
#         stickers_list.append(f"{robot_part} detail #{n}")
#     return stickers_list
# print(make_stickers(3, "Body"))

# def double_power(current_powers: list) -> list:
#     doubled = []
#     for power in current_powers:
#         doubled.append(power * 2)
#     return doubled
# print(double_power([100, 150, 200, 220]))

# def is_sorted(box_numbers: list) -> bool:
#     return all(box_numbers[i] <= box_numbers[i + 1] for i in range(len(box_numbers) - 1))
# print(is_sorted([]))

# def get_location(coordinates: list, commands: list) -> list:
#     for command in commands:
#         if command == "left":
#             coordinates[0] -= 1
#         elif command == "right":
#             coordinates[0] += 1
#         elif command == "forward":
#             coordinates[1] += 1
#         else:
#             coordinates[1] -= 1
#     return coordinates
# print(get_location([2, 3], ["back", "back", "back", "right"]))

# import math
# def get_plan(current_production: int, month: int, percent: int) -> list:
#     result_list = []
#     percent /= 100
#     print(percent)
#     for _ in range(month):
#         profit = math.floor(current_production * percent)
#         current_production += profit
#         result_list.append(current_production)
#     return result_list
# print(get_plan(10, 4, 30))

from math import floor
def get_speed_statistic(test_results: list) -> list:
    list_size = len(test_results)
    if list_size == 0:
        return [0, 0, 0]

    sum_of_all = 0
    min_speed = test_results[0]
    max_speed = test_results[0]

    for speed in test_results:
        sum_of_all += speed
        if speed > max_speed:
            max_speed = speed
        elif speed < min_speed:
            min_speed = speed

    avg = floor(sum_of_all / list_size)
    return [min_speed, max_speed, avg]

print(get_speed_statistic([9]))



