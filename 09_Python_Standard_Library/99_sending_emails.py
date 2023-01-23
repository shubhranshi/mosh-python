# In this lesson we will learn how to send emails in python.
# This is particularly useful if we have a database of customers, and we want to send them various emails
# based on their interests.
# We need to import 2 classes -
# one to create email messages, and another to connect with a SMTP server for sending email

from email.mime.multipart import MIMEMultipart
# In Python, we have a package "email" with a subpackage "mime" that stands for multipurpose internet mail extensions.
# This is a standard that define the format for email messages. It includes another subpackage multipart,
# that has MIMEMultipart class. The "MIMEMultipart" class allows as to send an email message that includes
# both html and plain text content. Depending upon what the client of email receiver supports,
# it can render either html content or plain text content.

# import the "MIMEText" class to attach a text or html to our email
from email.mime.text import MIMEText
# import the "MIMEImage" class to attach images to our email. We need to pass it as binary.
from email.mime.image import MIMEImage

# Importing the "smtplib" module to create a smtp server.
import smtplib

from pathlib import Path

message = MIMEMultipart()   # first we create MIMEMultipart object. After object is created, we need to set the headers
message["from"] = "Groot"
message["to"] = "shubhranshi.nthu1@gmail.com"
message["subject"] = "This is a test"
# These are various headers supported by MIMEMultipart object.

# To set the body, we need to attach the body to this message using "attach()" to attach a payload.
message.attach(MIMEText("Body"))
# by default set to plaintext content, we can set the content type to html by setting second argument as "html"
message.attach(MIMEImage(Path(r"C:\Users\user\Desktop\NTHU\DSC06758.jpg").read_bytes()))


# Now we have our mail message object "message" ready. We need to now send it using SMTP server.
# we need to create and open the SMTP and then close it. So it is better to use a "with" e.
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo() # This is a hello message to the smtp server. It's part of the smtp protocol (STEP 1)
    smtp.starttls() # This puts the smtp connection in TLS mode. now the transfer is secure (STEP 2)
    smtp.login("s109164422@m109.nthu.edu.tw", "blahblahbla")  # give login credentials  (STEP 3)
    smtp.send_message(message)  # send msg (STEP 4)
    print("Sent....")


# Remember the above concept... (code not able to execute: reason below)
# UPDATE: This feature is no longer supported as of May 30th, 2022.
# See https://support.google.com/accounts/answer/6010255?hl=en&visit_id=637896899107643254-869975220&p=less-secure-apps&rd=1#zippy=%2Cuse-an-app-password
# ORIGINAL ANSWER (No longer working): I ran into a similar problem and stumbled on this question.
# I got an SMTP Authentication Error but my user name / pass was correct. Here is what fixed it.
# I read this: https://support.google.com/accounts/answer/6010255
