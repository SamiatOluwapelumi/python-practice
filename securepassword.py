import random

characters=['?','/',',','><','"','[','}{','|','a','b','c','d','e','f','g','h','i','j','k','l','m','n,','o','p','q','r','s','t','u','v','w','x','y','z']
password_lenght=int(input('enter the lenth of your password: '))
random.shuffle(characters)
password=[]
for a in range(password_lenght):
    password.append(random.choice(characters))
random.shuffle(password)
print(''.join(password))
    