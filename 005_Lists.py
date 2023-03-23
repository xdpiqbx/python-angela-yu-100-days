# https://youtu.be/_uQrJ0TkZlc?t=6970

import random


# Any type of data in list
# Have an order

names = ['John', 'Hanna', 'Emmy', 'Bill', 'Sarah', "Elizabeth"]
print(names)
print(names[2])
print(names[-1])  # last item
print(names[2:])  # ['Emmy', 'Bill', 'Sarah', 'Elizabeth']
print(names[2:5])  # ['Emmy', 'Bill', 'Sarah']
print(names[1:4:2])  # ['Hanna', 'Bill'] # [from : to : step]
print(names[::-1])  # ['Elizabeth', 'Sarah', 'Bill', 'Emmy', 'Hanna', 'John'] # Reversed list

names.append("Batman!")

# It works like Srtings

# ----------------------------------------------- Exercise Find max
print("Exercise")
numbers = [3, 6, 2, 15, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if max < number:
        max = number
print(f'This is max number: {max}')

# ----------------------------------------------- 2D Lists

matrix =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for num in row:
        print(num)

# ----------------------------------------------- Lists functions

# numbers.append(20) # add item to list
# numbers.insert(0, 10) # insert(index_position_in_list, inserted_value)
# numbers.remove(15) # remove value 15 from the list
# numbers.clear() # remove all from list
# numbers.pop() # remove last item from the list
# numbers.index(15) # return index of 15 in list OR ValueError
# print(15 in numbers) # True or False if 15 in list
# numbers.count(4) # return numbers of value 4
# numbers.sort()
# numbers.reverse()
# copied_nums = numbers.copy()
# numbers.extend([23, 43, 65, 87, 88])

# ----------------------------------------------- Exercise Remove duplicates
print("Exercise")
ex_numbers = [3, 6, 2, 15, 8, 4, 10, 2, 6, 3]
new_list = []
for num in ex_numbers:
    if num not in new_list:
        new_list.append(num)
print(new_list)

# ----------------------------------------------- Unpacking
x, y, z, p, l, k, m, n, j, i = ex_numbers
print(f'Unpacking {x} {y} {z}')

# ----------------------------------------------- Split string
string = "Hello world Python here"
print(string.split(" "))
# ----------------------------------------------- Split string
string = "Angela, Ben, Jenny, Michael, Chloe"
names = string.split(", ")
loose = names[random.randint(0, len(names)-1)]
print(f"{loose} is going to buy the meal today!")

# ----------------------------------------------- Exercise

# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

column = int(position[0]) - 1
row = int(position[1]) - 1
map[row][column] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


