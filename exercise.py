import re
numRegex=re.compile(r'(\w\w)(\w)(\d)(\d\d\d\d\d\d)')
val=numRegex.findall('JOT1163250')
converted=val[0][0]+'-'+val[0][1]+'-'+val[0][2]+'-'+val[0][3]
print(converted)







# value='JOT1163250'
# # JO-T-1-163250
# b=[]
# c='-'
# for a in value:
#     b.append(a)
#     if a==value[1]:
#      b.append(c)
#     elif a==value[2]:
#      b.append(c)
#     elif a==value[3]:
#      b.append(c)
# print("".join(b))
    