from math import ceil
import time
import smtplib, ssl

def sendmail():
    smtp_server = "smtp.gmail.com"
    port = 587  
    sender_email = "pythonzealarax@gmail.com"
    password = 'znzucjqetqadells'
    fromaddr="pythonzealarax@gmail.com"
    toaddrs='oyinkansolaojelade1@gmail.com    '
    subject='YOU ARE COOKING SOMETHING?'
    text='Check on it now!'
    msg='subject:{}\n\n{}'.format(subject,text)
    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() 
        server.starttls() 
        server.ehlo() 
        server.login(sender_email, password)
        server.sendmail(fromaddr, toaddrs, msg)
    except Exception as e:
        print('hmn')
        print(e)
    finally:
        server.quit() 


i = 0
while (i < 1):
    food = input('What are you cooking? ')
    if (food.isalpha() == True):
        i = 1
        print('Your food is cooking')
    else:
        print('Invalid food type! Enter again')
        i = 0

t = 0
while (t < 1):
    timeNeeded = input('Enter cooking time in minutes:')
    if (timeNeeded.isnumeric() == True):
        # timeInSeconds = int(timeNeeded) * 60
        timeInSeconds = int(timeNeeded) * 5
        t = 1
    else:
        print('Invalid time! Enter again')
        t = 0

a = 0
while (a < 1):
    alarmPeriod = input('Enter preferred alarm period:')
    if ((alarmPeriod.isnumeric() == True) and (int(alarmPeriod) <= int(timeNeeded))):
        # alarmPeriodInSeconds = int(alarmPeriod) * 60
        alarmPeriodInSeconds = int(alarmPeriod) * 5
        a = 1
    else:
        print('Invalid alarm period! Enter again')
        a = 0

alarmFrequency = ceil(timeInSeconds / alarmPeriodInSeconds)
print(ceil(timeInSeconds / alarmPeriodInSeconds))
print('alerm will sound ', alarmFrequency, 'times')

# Method 1
cookedTime = 0
while (timeInSeconds - cookedTime >= 0):
    if (timeInSeconds - cookedTime >= alarmPeriodInSeconds):
        time.sleep(alarmPeriodInSeconds)

    else:
        time.sleep(timeInSeconds - cookedTime)

    cookedTime += alarmPeriodInSeconds
    print("You have something on the fire")
    sendmail()


print('Cooking completed')
sendmail()


