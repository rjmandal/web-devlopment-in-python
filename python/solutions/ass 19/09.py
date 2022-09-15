'''9. Write a python program to create a function to check whether 
a number falls in a given range.'''


def check(r):
    n=4
    for e in r:
        if n==e:
            print("yes")
            break
    else:
        print("no")             

check(range(int(input("enter the begning of the range ==>> ")),int(input("enter the ending of the range ==>> "))+1))
