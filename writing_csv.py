import csv
header=['NAME  ','GRADE']
datas=[['SHERIFAT','A'],['HABEEB','A'],['DEV TOLU','A'],['THING','C'],['EWEE','B'],['AYII','D'],['DIDI','F'],['SAMIAT','A']]

with open ('new_grade.csv','w',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(header)
    writer.writerows(datas)