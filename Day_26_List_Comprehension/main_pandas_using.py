import pandas

stud_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

student_data_frame = pandas.DataFrame(stud_dict)
print(student_data_frame)
#   student  score
# 0  Angela     56
# 1   James     76
# 2    Lily     98


for (key, value) in student_data_frame.items():
    print(key)
# student
# score

for (key, value) in student_data_frame.items():
    print(value)
# 0    Angela
# 1     James
# 2      Lily
# Name: student, dtype: object
# 0    56
# 1    76
# 2    98
# Name: score, dtype: int64

for (key, value) in student_data_frame.iterrows():
    print(value)
# student    Angela
# score          56
# Name: 0, dtype: object

# student    James
# score         76
# Name: 1, dtype: object

# student    Lily
# score        98
# Name: 2, dtype: object

for (key, value) in student_data_frame.iterrows():
    print(value.student)
# Angela
# James
# Lily