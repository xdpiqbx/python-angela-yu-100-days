import os
import smtplib
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()


class NotificationManager:

    def __init__(self, data):
        self.sender = os.environ["MAIN_MAIL"]
        self.password = os.environ["GOOGLE_APP_PWD"]
        self.data = data

    def send_email(self):
        msg = MIMEText(self.prepare_body(), 'html')
        msg['Subject'] = f"Message from you blog. Sender - {self.data.get('name')}"
        msg['From'] = self.sender
        msg['To'] = ', '.join([os.environ["SECONDARY_MAIL"]])
        with smtplib.SMTP_SSL('smtp.gmail.com', port=465) as connection:
            connection.login(
                user=self.sender,
                password=self.password
            )
            connection.sendmail(
                from_addr=self.sender,
                to_addrs=[os.environ["SECONDARY_MAIL"]],
                msg=msg.as_string()
            )

    def prepare_body(self):
        return (f"<hr>"
                f"Sender name: {self.data.get('name')}<br>"
                f"Email: {self.data.get('email')}<br>"
                f"Phone: {self.data.get('phone')}<br>"
                f"Message: {self.data.get('message')}<br>"
                f"<hr>")
