import random
# alpha=['0','1','2','3','4','5','6','7','8','9',
#        'a','b','c','d','e','f','g','h','i','j',
#        'k','l','m','n','o','p','q','r','s','t',
#        'u','v','w','x','y','z',]

# def find_missing(s):
#     m=[]
#     for i in s:
#        m.append(i)
#     m=list(set(m))
#     # print(m)
#     for j in m:
#         alpha.remove(j)
#     c=''
#     for k in alpha:
#         c=k+c
#     c=sorted(c)
#     c=''.join(c)        
#     print (c)

# inp=input('Enter string: ')

# find_missing(inp)

# def simpleArraySum(ar):
#     total=0
#     for sum in ar:
#         total=total+sum
#     print(total)
#     # Write your code here
# simpleArraySum(ar=[1,2,3])

# def compareTriplets(al, bo):
#     alice=0
#     bob=0
    # for a in al:
    #     # print('.')
    #   for b in bo:
    #     print(a,b)
    #     if a>b:
    #         alice=alice+1
    #         print('alice point is:',alice)
    #     elif a<b:
    #         bob=bob+1
    #         print('bob point is:',bob)
    #     elif a==b:
    #         alice=alice+0
    #         bob=bob+0
    # for i in range(len(al)):
    #     if(al[i] == bo[i]): 
    #         alice+= 0
    #         bob+= 0
    #     elif(al[i] > bo[i]):
    #         alice+= 1
    #     elif(al[i] < bo[i]):
    #         bob+= 1;
    # return [f"Alice score is {alice}", f"Bob score is {bob}"]
# print(compareTriplets( [1, 2, 3], [3, 2, 1]))


# def diagonalDifference(arr):
#     # Write your code here
#     a = 0
#     b = 0
#     i,j = 0,0
#     while i< len(arr) and j < len(arr):
#         a += arr[i][j]
#         i+=1
#         j+=1
#     m,n = len(arr)-1,0
#     while m >=0 and n<len(arr):
#         b+= arr[m][n]
#         m-=1
#         n+=1
#     return abs(a-b)



# def aVeryBigSum(ar):
#     # Write your code here
#     ar=[5,1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
#     a=0
#     for b in range(len(ar)) :
#         a=a+ar[b]
#         print(a)
# aVeryBigSum([5,1000000001, 1000000002, 1000000003, 1000000004, 1000000005])



from itertools import count


# array=[1, -2 ,-7, 9 ,1, -8, -5]
# minus=[]
# zero=[]
# plus=[]
# m=0
# z=0
# p=0
# b=len(array)
# for a in array:
#     if a<0:
#         minus.append(a)
#         m=len(minus)
#     elif a==0:
#         zero.append(a)
#         z=len(zero)
#     elif a>0:
#         plus.append(a)
#         p=len(plus)
# print("{:.6f}".format(m/b),'\n',"{:.6f}".format(z/b),'\n',"{:.6f}".format(p/b))


# def staircase(n):
#     # Write your code here
#     # n=int(input('enter n: '))
#     b='#'
#     i = n - 1
#     for a in range(1, n + 1):
    
#         print(' '*i+ a * b.strip())
#         i = i - 1
        
# if __name__ == '__main__':
#     n = int(input().strip())
#     staircase(n)

# arr=[3,5,4,2,1]
# arr.sort()
# # print(arr)
# min=0
# max=0
# # for a in range (len(arr)-1):
# for a in arr[:-1]:
#   min=min+a
# for b in arr[1:]:
#     max=max+b
# print(min,max)


# candles=[3, 2, 1, 3]
# b=(max(candles))
# max=[]
# for a in candles:
#     if a==b:
#       max.append(a)
        
# print(len(max))

# a=input('time: ')
# if a[-2:]=='AM' and a[:2]=='12':
#     print('00'+a[2:-2])
# elif a[-2:]=='AM':
#     print(a[:-2])
# elif a[-2:]=='PM' and a[:2]=='12':
#     print(a[:-2])
# else:
#     print(str(int(a[:2])+12)+a[2:8])



# def filledOrders(order, k):
#     # Write your code here
#     total = k
#     fulf = []
#     for r in order:
#         if r <= total:
#             fulf.append(r)
#             total -= r
#         else:
#             break

#     if sum(fulf) > k:
#         fulf.pop()
        
#     return len(fulf)



# def findSum(numbers, queries):
#     # Write your code here
#     if not isinstance(numbers, list) and not isinstance(queries, list):
#         return
#     result = []
#     total = 0
#     for query in queries:
#         if len(query) == 3:
#             start = query[0]
#             end = query[1]
#             additional = query[2]
#             selection = numbers[start-1:end]
#             has_zeros = False
#             for el in selection:
#                 if el == 0:
#                     has_zeros = True
#             print(f"has_zeros: {has_zeros}")
#             print(f"selection: {selection}")
#             total = sum(selection)
#             if has_zeros:
#                 total += additional
#             result.append(total)
#     return result


