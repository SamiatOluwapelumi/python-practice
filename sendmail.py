import smtplib, ssl
# port=465
# password='znzucjqetqadells'
# context=ssl.create_default_context()

# with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
#     server.login('pythonzealarax@gmail.com', password)


smtp_server = "smtp.gmail.com"
port = 587  
sender_email = "pythonzealarax@gmail.com"
password = 'znzucjqetqadells'
fromaddr="pythonzealarax@gmail.com"
toaddrs='amobeeb1net@gmail.com'
msg='hello world'
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
