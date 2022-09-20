'''3. Write a recursive python function to print first N odd odd numbers'''

def odd(n):
    if n>0:
        odd(n-1)
        print(n*2-1)

odd(int(input("enter a no ==>> ")))