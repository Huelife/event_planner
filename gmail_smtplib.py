#gmail_smtplib.py: Sending gmail through smtplib

import smtplib

from email.mime.text import MIMEText

with open("msg.txt","r") as fin:
    msg_rd = fin.read()
    msg = MIMEText(msg_rd)

#getting email username/password and from/to email address
username = input("Username: ")
password = input("Password: ")
email_from = input("From: ")
email_to = input("To: ")

#email format function
def gmail_format():
  msg["Subject"] = "Event Planner"
  msg["From"] = email_from
  msg["To"] = email_to

#sending email through smtp function
#gmail access for less secure apps must be ENABLED
def gmail_send():
  gmail = smtplib.SMTP("smtp.gmail.com",587)
  gmail.ehlo()
  gmail.starttls()
  gmail.ehlo()
  gmail.login(username,password)
  gmail.sendmail(email_from,email_to,msg.as_string())
  gmail.quit()

gmail_format()
gmail_send()
