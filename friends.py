# import csv 
# f=open('friends.csv','r')
# save=[]
# with f:
#     reader=csv.reader(f)
#     for row in reader:
#         for e in row:
#          save.append(e)
    
#     for a in save:
#         print(a)


import string

# def missingCharacters(s):
    # s=samiat2000
s='8hypothetical'
missing_char=[]
a=string.ascii_lowercase 
b=string.digits
    # print(a,b)
for i in range (len(s)):
    x=ord(s[i])
    if s not in char:
      missing_char.append(char)
print(missing_char)
            
# missingCharacters('8hypothetical')