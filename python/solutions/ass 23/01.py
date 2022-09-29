'''1. Use iter and next method to access all the elements of a given set using while loop'''

s={1,2,3,4,5,6,7,8}
it=iter(s)
l=len(s)
while l:
    print(next(it))
    l-=1
