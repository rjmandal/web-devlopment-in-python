'''7. Write a recursive python function to print squares of first N natural numbers'''

def square(n):
    if n>0:
        square(n-1)
        print(n**2)

square(int(input("enter a no ==>> ")))