import os
import smtplib
from email.mime.text import MIMEText

from dotenv import load_dotenv
load_dotenv()


class NotificationManager:

    def __init__(self):
        self.sender = os.environ["MAIN_MAIL"]
        self.password = os.environ["GOOGLE_APP_PWD"]

    def send_email(self, body, recipients):
        msg = MIMEText(body, 'html')
        msg['Subject'] = "На деякі товари знижено ціну"
        msg['From'] = self.sender
        msg['To'] = ', '.join(recipients)
        with smtplib.SMTP_SSL('smtp.gmail.com', port=465) as connection:
            connection.login(user=self.sender, password=self.password)
            connection.sendmail(from_addr=self.sender, to_addrs=recipients, msg=msg.as_string())
