import csv 
f=open('friends.csv','r')
save=[]
with f:
    reader=csv.reader(f)
    for row in reader:
        for e in row:
         save.append(e)
    
    for a in save:
        print(a)
