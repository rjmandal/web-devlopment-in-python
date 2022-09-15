'''8. Write a python program to multiply all the numbers in a list.'''


def multi(l):
    r=1
    for e in l:
        r=e*r             
    print(r)


multi([int(e) for e in input("enter the no seperated by comma ==>> ").split(",")])
