import time
import webbrowser

url=input('enter your website url: ')
alerm=input('set website alerm in H:M:S: ')
time_now=time.strftime('%H:%M:%S')
print(time_now)
print(alerm)
while (alerm!=time_now):
    print('the time is \n',time_now)
    time_now=time.strftime('%H:%M:%S')
    time.sleep(1)
    if (alerm==time_now):
        
        print ("You should see your webpage now :-)")
        webbrowser.open(url)
