'''8. Write a python program to create a function that accepts a string and calculate the
number of upper case letters and lower case letters.'''

def nunl(s):
    l=0
    u=0
    for e in s:
        if e.islower():
            l+=1
        elif e.isupper():
            u+=1
    return l,u

lower,upper=nunl(input('enter the string ==>> '))
print(lower,upper)