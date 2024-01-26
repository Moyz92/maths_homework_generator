import os
from datetime import datetime
import smtplib as smt
from email.message import EmailMessage
from homework import make_homework

message = make_homework()

current_hour = datetime.now().strftime("%I%p")
my_email = os.environ.get('EMAIL_ADDRESS')
password = os.environ.get('PASSWORD')


msg = EmailMessage()
msg['Subject'] = "Your Homework is here!!"
msg['From'] = my_email
msg['To'] = 'moyzahmed2020@gmail.com'
msg.add_alternative(message.get_template(), subtype='html')

with smt.SMTP_SSL('smtp.gmail.com', port=465) as connection:
    connection.login(user=my_email, password=password)
    connection.send_message(msg)