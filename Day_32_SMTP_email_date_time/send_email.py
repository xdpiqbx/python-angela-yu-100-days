import os
import smtplib
from email.mime.text import MIMEText

from dotenv import load_dotenv
load_dotenv()

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', port=465) as connection:
        connection.login(user=sender, password=password)
        connection.sendmail(from_addr=sender, to_addrs=recipients, msg=msg.as_string())

send_email(
    subject="Email Subject",
    body="This is the body of the text message\nCall me later =) 465-65-44",
    sender=os.environ["MAIN_MAIL"],
    recipients=[os.environ["SECONDARY_MAIL"]],
    password=os.environ["GOOGLE_APP_PWD"],
)
