import numpy as np
# my_data=[[1,3,2],[4,7,5],[6,2,4]]
# ar=np.array(my_data)
# for a in ar:
#     print('  '.join(map(str,a)))

x=[[7,9,0],
   [4,6,5],
   [2,3,6]]

y=[[9,0,8],
   [5,4,6],
   [3,2,1]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(x)):
    for j in range(len(y)):
        result[i][j]=x[i][j]+y[i][j]
for r in result:
    a=('  '.join(map(str,r)))
    print(a)