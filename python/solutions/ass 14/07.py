'''7. Write a Python script to remove all non int values from a list.'''

l=["sanjay",23,199,"mandal",3+4j,True,4.5,6]
print("list ==>> ",l)
 
n=len(l)
i=0
while i<n:
    if type(l[i])!=int:
        del(l[i])
        n-=1
    else:
        i+=1
print("result ==>> ",l)

''' alternate method by making new list '''

l1=[]
for i in l:
    if type(i)==int:
        l1.append(i)
print("result ==>> ",l1)