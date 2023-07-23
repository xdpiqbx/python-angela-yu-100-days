customer = {
    "name": "John",
    "age": 30,
    "is_verified": True,
    # "name": "Olof", # name already exists, it will reassign name!
}

print(customer.items())  # dict_items([('name', 'John'), ('age', 30), ('is_verified', True)])
print(customer.values())  # dict_values(['John', 30, True])
print(customer.keys())  # dict_keys(['name', 'age', 'is_verified'])
print(customer.get("age"))  # 30 or None if age not exists

customer["birthday"] = "Jan 1 1980"  # Add new field to dict

print("=========================")

for key in customer.keys():
    print(customer[key])

print("=========================")

for key in customer:
    print(customer[key])

print("=========================")
# --------------------------------- Exercise

nums = {
    '0': "Zero",
    '1': "==1==",
    '2': "==2==",
    '3': "==3==",
    '4': "==4==",
    '5': "==5==",
    '6': "==6==",
    '7': "==7==",
    '8': "==8==",
    '9': "==9==",
}

# phone = input("Phone: ")
# str = ""
# for digit in phone:
#     str += nums.get(digit, "!") + " "
# print(str)

# --------------------------------- Nested Dictionaries
travel_log1 = {
    "France": {
        "cities_visited": ["Paris", "Lile", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 10
    }
}

travel_log2 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lile", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 10
    }
]

# --------------------------------- Smile converter
# message = input("Input text with smile > ")
# words = message.split(' ')
# emojis = {
#     ":)": "😊",
#     ":(": "😞"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

# --------------------------------- Exercise
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}
for name in student_scores:
    if student_scores[name] > 90:
        student_grades[name] = "Outstanding"
    elif student_scores[name] > 80:
        student_grades[name] = "Exceeds Expectations"
    elif student_scores[name] > 70:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"

print(student_grades)

# --------------------------------- Exercise 2 - Dictionary in List

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country, visits, cities):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities
    })


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])  # Steak

# Task Blind Auction
