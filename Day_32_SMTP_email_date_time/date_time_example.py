# import datetime as dt
from datetime import datetime

now = datetime.now()  # 2023-04-03 19:44:43.777141
print(now.year)  # 2023
print(now.weekday())  # 0 - Monday

dt = datetime(year=1990, month=12, day=31)
print(dt)
