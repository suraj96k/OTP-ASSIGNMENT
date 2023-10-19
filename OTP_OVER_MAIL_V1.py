# OTP to mail

import smtplib
import random

sender = "surajkhaire9696k@gmail.com"
password = "ijmv wvdz duei usah"
receiver = "surajkhaire8055@gmail.com"
body = "Your OTP is " + str(random.randint(100000, 999999)) + ". Valid for next 15 minutes."

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(sender, password)

server.sendmail(sender, receiver, body)

print("Mail sent")