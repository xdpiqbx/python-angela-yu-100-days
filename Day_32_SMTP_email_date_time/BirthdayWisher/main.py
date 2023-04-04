import random
from datetime import datetime

import pandas

BIRTHDAYS_CSV_FILE = "./birthdays.csv"

LETTERS = [
    "./letter_templates/letter_1.txt",
    "./letter_templates/letter_2.txt",
    "./letter_templates/letter_3.txt"
]

birthdays_dict = pandas.read_csv(BIRTHDAYS_CSV_FILE).to_dict(orient="records")

def is_today(birthday, today):
    return birthday["day"] == today.day and birthday["month"] == today.month

def send_email(subject, body, sender, recipients, password):
    return {
        "subject": subject,
        "body": body,
        "sender": sender,
        "recipients": recipients,
        "password": password
    }

birthdays_today = [birthday for birthday in birthdays_dict if is_today(birthday, datetime.now())]

for birthday in birthdays_today:
    with open(random.choice(LETTERS)) as letter_file:
        content = letter_file.read().replace("[NAME]", birthday["name"])

        print(send_email(
            f"Happy Birthday {birthday['name']}",
            content,
            "my_email@mail.com",
            birthday['email'],
            "p@ssworD"
        ))
