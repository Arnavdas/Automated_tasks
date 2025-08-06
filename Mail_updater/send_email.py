import smtplib
from email.message import EmailMessage
import os

def send_email(tym_now=''):
    msg = EmailMessage()
    msg["Subject"] = "Daily Notification"
    msg["From"] = os.getenv("EMAIL_ADDRESS")
    msg["To"] = os.getenv("RECIPIENTS")  # comma-separated list
    msg.set_content(f"This is your daily {tym_now} notification.")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_PASSWORD"))
        smtp.send_message(msg)

if __name__ == "__main__":
    send_email()
