# Author  : Deepansh Dubey.
# Date    : 30-Aug-2020.
# Purpose : Sending the health status of a patient to their family member's phone number and email.


import pandas as pd
import datetime
import smtplib
from smtplib import SMTP
import requests
import json

# EMAIL CREDENTIALS
GMAIL_ID = "exm@exp.com"
GMAIL_PSWD = "password"

def sendEmail(to, name, sub, msg):
    print(f"Email sent to {to} with subject: {sub} and message {msg}")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to,f"subject: {sub}\n\n This is to inform you that Mr. {name} is {msg}")
    s.quit()

def sendSMS (number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {"authorization":"key","sender_id":"FSTSMS","message": message,"language":"english","route":"p","numbers":number}
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)
    
if __name__ == "__main__":
    df = pd.read_excel("data.xlsx")
    today = datetime.datetime.now().strftime("%d-%m-%Y")

    for index, item in df.iterrows():
        # print(index, item['Completion'])
        day = item['Completion'].strftime("%d-%m-%Y")
        # print(day)
        if(today == day):
            sendEmail(item['Email'], item['Name'], "Current Health Status", item['Status'])
            sendSMS(item['Number'], "This is to inform you that Mr." + item['Name'] + " is " + item['Status'])

           
