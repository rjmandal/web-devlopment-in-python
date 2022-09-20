'''9. Write a recursive python function to print first N multiples of a given number.'''

def nmultiple(n,m):
    if m>0:
        nmultiple(n,m-1)
        print(m*n)

nmultiple(int(input("enter a no ==>> ")),int(input("enter no of multiples ==>> ")))