'''6. Write a recursive python function to print first N even natural numbers in reverse
order.'''

def even(n):
    if n>0:
        print(n*2)
        even(n-1)

even(int(input("enter a no ==>> ")))