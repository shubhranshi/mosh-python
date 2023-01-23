from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from pathlib import Path

# In previous lecture, the body of an email was added along with the rest of the code.
# But in actual, the body of an email can be several lines of text. All this text cant be included
# along with other lines of code. Quite often, we put that text in a separate file as a template and
# we use HTML to build that template.
# In this section, we discuss how to create and use templates.
# Templates should be named according to the scenarios where they are to be used.
# create "template.html"

# import the "Template" class to replace the parameter in the template string ($user in "template.html")
from string import Template

template = Template(Path("template.html").read_text())
# We are returning the content of the "template.html" as a string
# this template object has a method substitute() that can be used to replace parameters dynamically

message = MIMEMultipart()   # first we create MIMEMultipart object. After object is created, we need to set the headers
message["from"] = "Groot"
message["to"] = "shubhranshi.nthu1@gmail.com"
message["subject"] = "This is a test"

# We create the email body, and substitute the "$" parameter of the template ("template.html")
# with the ".substitute" method, using a dictionary or keyword arguments.
email_body = template.substitute({"first_name": "Shubhranshi", "last_name": "Kapoor"})  # we can pass a dictionary
message.attach(MIMEText(email_body, "html"))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp: # use "with" statement to create, open & then close SMTP.
    smtp.ehlo() # This is a hello message to the smtp server. It's part of the smtp protocol (STEP 1)
    smtp.starttls() # This puts the smtp connection in TLS mode. now the transfer is secure (STEP 2)
    smtp.login("s109164422@m109.nthu.edu.tw", "blahblahbla")  # give login credentials  (STEP 3)
    smtp.send_message(message)  # send msg (STEP 4)
    print("Sent....")




