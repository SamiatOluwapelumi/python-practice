# def myfunction(fname):
#     print(fname , 'samiat')
# myfunction('oshoko')
# myfunction('odeyemi')
# myfunction('lasisi')

# def myname(fname,lname):
#     print(fname+' '+lname)
# myname('oshoko', 'samiat')

# def myfunction(*kids):
#     print('the youngest kid is', kids[2])
# myfunction('samiat','muslimah','fadhlullah')

# def realname(child1,chiled2,child3):
#     print('the youngest kid is', child3)
# realname(child1='samiat',chiled2='muslimah',child3='fadhlullah')


# def lname(**kids):
#     print("His last name is " + kids["lname"])
# lname(fname='fadhlullah', lname='odeyemi')

# def country(country='nigeria'):
#     print('i am from', country)
# country('sweden')
# country('norway')
# country()
# country('brazil')

# def myfunction(food):
#     for x in food:
#         print(food)
# fruit=['apple','banana','orange','guava']
# myfunction(fruit)

# def myfunction(x):
#     return (5*x)
# print(myfunction(5))
# print(myfunction(4))
# print(myfunction(7))

# def myfunction():
#     pass

def tri_recursion(k):
    if (k>0):
        result=k+tri_recursion(k-1)
        print(result)
    else:
        result=0
    return result
print('\n\nRecursion example results')
tri_recursion(6)

