import os
import smtplib
from email.mime.text import MIMEText
import random
from datetime import datetime

QUOTES = "./quotes.txt"

def get_number_of_lines_in_file(file):
    quotes_count = 0
    with open(file) as quotes:
        while True:
            if not quotes.readline():
                break
            quotes_count += 1
    return quotes_count

def get_random_quote():
    quote_random_line_index = random.randint(1, get_number_of_lines_in_file(QUOTES))
    with open(QUOTES) as quotes:
        quotes_count = 0
        while True:
            quotes_count += 1
            if quotes_count == quote_random_line_index:
                return quotes.readline()
            quotes.__next__()

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', port=465) as connection:
        connection.login(user=sender, password=password)
        connection.sendmail(from_addr=sender, to_addrs=recipients, msg=msg.as_string())

is_monday = datetime.now().weekday() == 0

if is_monday:
    send_email(
        subject="Mondays Motivational Quotes",
        body=get_random_quote(),
        sender=os.environ["MAIN_MAIL"],
        recipients=[os.environ["SECONDARY_MAIL"]],
        password=os.environ["PWD"],
    )
