'''2. Write a recursive python function to print first N natural numbers in reverse order'''

def natural(n):
    if n>0:
        print(n)
        natural(n-1)

natural(int(input("enter a no ==>> ")))