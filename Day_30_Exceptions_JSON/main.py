# try:
#     file = open("file.txt")
#     some_dict = {"key": "value"}
#     print(some_dict["key"])
# except FileNotFoundError:
#     #  if File not found
#     file = open("file.txt", "w")
#     file.write("Some content")
# except KeyError as error_message:
#     print(f"The key: [{error_message}] does not exists")
# else:
#     # this block will work if in try all Ok
#     content = file.read()
#     print(f"In else block. {content}")
# finally:
#     file.close()
#     print("finally block")
#     raise TypeError("this is my error")
import json

# ****************************************** Task catch IndexError
# fruits = ["Apple", "Pear", "Orange"]
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
# make_pie(4)

# ****************************************** Task catch KeyError
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
# total_likes = 0
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass
#         # total_likes = total_likes + 0
# print(total_likes)

# ****************************************** JSON
# write - json.dump(data, data_file, indent=4)
# read - json_dict = json.load(data_file)
# update - json_dict.update(data)

# To update:
# 1. (open for read) read;
# 2. update;
# 3. write
