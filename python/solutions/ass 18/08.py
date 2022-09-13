'''8. Write a python program to convert two lists into a dictionary in a way that item from
list1 is the key and item from list2 is the value.'''


list1=[1,2,3,4,5,6]
list2=["sanjay","suraj","kajal","raju","suar","ravi"]
d={}
for e in range(6):
    # d[eval(list2[e])
    d[list1[e]]=list2[e]
print(d)

