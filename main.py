from email.message import EmailMessage
import ssl
import smtplib

sender = "[Email-Sender]"
reciver = "[Email-Reciver]"
password = "[password]"
ms = EmailMessage()
ms["from"]= sender
ms["to"] = reciver
ms["subject"] = "you are strong man"

ms.set_content('I want to tell to something that make you happy')


context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(sender,password= password)
    smtp.sendmail(sender,reciver,ms.as_string())

