'''7. Write a python script to determine whether a string 
contains a specific substring.'''

String= input("enter your name ==>> ")
SubString =input("enter a sub string for search ==>> ")
for e in String:
    if e==SubString:
        print("sub string is present ")
        break
else:
    print("sub string is not present ")