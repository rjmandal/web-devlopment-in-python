'''3. Write a python program to create a function which expects an unknown number of
arguments.'''

def arg(*t):
    for e in t:
        print(e,end=" ")

arg(23,34,45,67,55)
arg(23,34)
arg(23,34,45,55)
arg(23,34,45,67,55,44,33,5,34,6,7,8,9,7,6)