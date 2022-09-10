'''8. Write a python program to Sort a tuple of tuples by the second item.
tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))'''

tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
# print(sorted(tuple1)) 
n=len(tuple1)
i=0
while n-1:
    if tuple1[i][1]>tuple1[i+1][1]:
        tuple1[i],tuple1[i+1]=tuple1[i+1],tuple1[i]
    i+=1
print(tuple1)