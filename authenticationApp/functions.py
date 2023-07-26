from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
# Import Packages For Email
from email.message import EmailMessage
import ssl
import smtplib



#> This Function Take Handle of password matching and check password Length
def userCreationChecker(firstname , lastname ,email,password,password_conf):
    username_length = len(firstname) >= 3 and len(lastname) >= 3
    passwordLength = len(password) >= 8
    password_matching = (password == password_conf)
    if (username_length and email and passwordLength and password_matching):
        return True
    return False



#> This Function is used to check if the user is already exist
def checkUserExists(username):
    try:
        user = User.objects.get(username=username)
        return True
    except User.DoesNotExist:
        return False



#> This function is used to send Email
def sendEmail(email_receiver,subject,body):
    email_sender = "mehdihyad.mh@gmail.com"
    email_password = "f a e h l s u h l m h y v b a x"
    emailMessage = EmailMessage()
    emailMessage['From'] = email_sender
    emailMessage['To'] = email_receiver
    emailMessage['Subject'] = subject
    emailMessage.set_content(body)

    # Define Smtp connection
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465 , context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, emailMessage.as_string())
        return True