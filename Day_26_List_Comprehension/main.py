numbers = [1, 2, 3, 4, 5]
new_nums = [item + 1 for item in numbers]
print(new_nums)

name = "dpiqb"
name_arr = [letter for letter in name]
print(name_arr)

doubled_range = [i * 2 for i in range(1, 5)]
print(doubled_range)

# Conditional List Comprehension

even_range = [i for i in range(1, 25) if i % 2 == 0]
print(even_range)

names = ["Caroline", "Alex", "Beth", "Dave", "Eleanor", "Freddie"]
long_caps_names = [name.upper() for name in names if len(name) > 5]
print(long_caps_names)


# Exercise 1 - Squaring Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)

# Exercise 2 - Filtering Even Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num % 2 == 0]
print(result)

# Exercise 3 - Data Overlap
print("Exercise 3 - Data Overlap")
with open("file1.txt") as file1:
    content1 = file1.readlines()
with open("file2.txt") as file2:
    content2 = file2.readlines()
new_list = [int(item) for item in content1 if item in content2]
print(new_list)

# Exercise 4 - Dictionary Comprehension 1
print("Exercise 4 - Dictionary Comprehension 1")
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split(" ")}
print(result)

# Exercise 5 - Dictionary Comprehension 2
print("Exercise 5 - Dictionary Comprehension 2")
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp * 9/5 + 32) for (day, temp) in weather_c.items()}
print(weather_f)
