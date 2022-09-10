'''8. Write a python program to Sort a tuple of tuples by the second item.
tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))'''

tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
l=[e for e in tuple1]
n=len(l)
n1=n-1
print(n) 
while n1:
    i=0
    while n-1:
        if l[i][1]>l[i+1][1]:
            l[i],l[i+1]=l[i+1],l[i]
        i+=1
        n-=1
    n1-=1
tuple1=tuple([e for e in l])
print(tuple1,type(l))