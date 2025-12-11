import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv


load_dotenv()

GMAIL_USER = os.getenv('GMAIL_USER')
GMAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')

message = MIMEMultipart("alternative")

    
def send_email(subject, body, to_email, email, password):
    my_server = smtplib.SMTP('smtp.gmail.com', 587)
    my_server.starttls()
    my_server.ehlo()
    my_server.login(email, password)
    
    message = MIMEMultipart("alternative")
    message['Subject'] = subject
    message['From'] = email
    message['To'] = to_email

    text_content = body
    part1 = MIMEText(text_content, "plain")
    message.attach(part1)
    my_server.sendmail(email, to_email, message.as_string())
    my_server.quit()
