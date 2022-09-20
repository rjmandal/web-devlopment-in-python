'''4. Write a recursive python function to print first N odd natural numbers in reverse order'''

def odd(n):
    if n>0:
        print(n*2-1)
        odd(n-1)

odd(int(input("enter a no ==>> ")))