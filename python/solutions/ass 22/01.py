'''1. Write a recursive python function to calculate sum of first N natural numbers'''

def add(n):
    if n==1:
        return 1
    return n+add(n-1)
    
print(add(int(input("enter the no ==>> "))))