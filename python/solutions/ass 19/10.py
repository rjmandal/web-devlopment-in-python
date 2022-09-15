'''10. Write a python program to create a function to check whether a given number is even
or odd.'''


def check(n):
    if n%2:
        print("odd")
    else:
        print("even")             

check(int(input("enter the no ==>> ")))
