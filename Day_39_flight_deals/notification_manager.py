import os
import smtplib
from email.mime.text import MIMEText
class NotificationManager:
    #  This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.sender = os.environ["MAIN_MAIL"]
        self.password = os.environ["GOOGLE_APP_PWD"]

    def send_email(self, body, recipients):
        msg = MIMEText(body)
        msg['Subject'] = "Hot offers"
        msg['From'] = self.sender
        msg['To'] = ', '.join(recipients)
        with smtplib.SMTP_SSL('smtp.gmail.com', port=465) as connection:
            connection.login(user=self.sender, password=self.password)
            connection.sendmail(from_addr=self.sender, to_addrs=recipients, msg=msg.as_string())
