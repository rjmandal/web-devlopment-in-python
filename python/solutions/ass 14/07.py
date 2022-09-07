'''7. Write a Python script to remove all non int values from a list.'''

l=["sanjay",23,199,"mandal",3+4j,True,4.5]
print("list ==>> ",l) 


'''l1=[]
for i in l:
    if str(type(i))=="<class 'int'>":
        print(l.index(i))
        l1.append(i)
print("result ==>> ",l1)'''


l1=[]
for i in l:
    if str(type(i))=="<class 'int'>":
        print(l.index(i))
        l1.append(i)
print("result ==>> ",l1)