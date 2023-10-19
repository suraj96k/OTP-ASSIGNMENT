#Importing requires libraries
import random
import re
import smtplib
from twilio.rest import Client

#User and Twilio info
account_sid = 'AC8480c4d66f0ff04c7652a274cf198391'
auth_token = '65d15e5d667fa26fc7d3713a94b78ab0'
client = Client(account_sid, auth_token)
twilio_num = '+18155590856'
target = '+917888008055'

#Function to generate OTP
def generateOtp(n = 6):
    otp = ""

    for i in range(n):
        otp += str(random.randint(0, 9))
    
    return otp

#Function to validate mobile
def validateMobile(mobile):
    return len(mobile) == 10 and mobile.isdigit()

#Function to validate Email
def validateEmailID(receiver):
    # not efficient way
    # if "@" not in receiver or "." not in receiver:
    #     return False
    # return True

    #efficient way - good practice
    validation_condition = r"^[\w\.-]+@[\w\.-]+\.\w+$"  # validation using regular expression
    if re.search(validation_condition, receiver):
        return True
    else:
        return False

# Send OTP over mobile using Twilio
def sendOTPOverMobile(target, otp):
    if(validateMobile(target)):
        target = "+91" + target
        message = client.messages.create(
            body = "Your OTP is " + otp + ". Valid for next 15 minutes.",
            from_= twilio_num,
            to=target
        )

        print(message.body)
        print("Check Phone! Sent to ", target)
    else:
        print("Enter valid mobile number!!")

# Send OTP over email using SMTP
def sendOTPOverEmail(receiver, otp):
    body = "Your OTP is " + otp + ". Valid for next 15 minutes."

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, body)

    print("Mail sent - OTP: ", otp)


#Driver Code
if __name__ == "__main__":

    print("Welcome to Random OTP sender!!\nHere, we send random OTPs to phone number and mails.\n")

    sender = "shubhankar.gokhale25@gmail.com"
    password = "khlgazxcrltifoec"
    # User input for email
    receiver = input("Enter mail: ")

    #create a unique Otp
    otp = generateOtp(6)

    #Send OTP over Email
    if(validateEmailID(receiver)):
        sendOTPOverEmail(receiver, otp)
    else:
        print("Please Enter valid mail!!")


    #Send OTP over SMS
    send_twilio = input("\nDo you want to send OTP via SMS: ")
    if send_twilio.lower() == "yes":
        # User input for mobile
        target = input("Enter mobile: ")

        sendOTPOverMobile(target, otp)
        
        print("\nOTP sending program ended\n")
    else:
        print("OTP sending program ended")

    #Program Ended