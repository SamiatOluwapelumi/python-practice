import csv
with open('SCORE.CSV') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    for row in csv_reader:
        if (row[0]=='NAME') and (row[1]=='SCORE'):
            continue
        score=int(row[1])
        name=row[0]
        def gradeFunction(name,score):
            if(score >=70 and score <=100):
                return f'{name} got an "A"'
            elif (score>=60 and score<=69):
                return f'{name} has a "B"'
            elif (score>=50 and score<=59):
                return f'{name} has a "C"'
            elif (score>=40 and score<=49):
                return f'{name} has a "D"'
            elif (score>=10 and score<=39):
                return f'{name} has an "F"'
            else:
                return "i do not know your grade"
        print(gradeFunction(name,score))
