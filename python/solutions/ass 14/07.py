'''7. Write a Python script to remove all non int values from a list.'''

l=["sanjay",23,199,"mandal",3+4j,True,4.5]
print("list ==>> ",l)
for e in l:
    print(type(e))
    # if e
    del e
print(l)