'''2. Write a recursive python function to calculate sum of first N odd natural numbers'''

def addodd(n):
    if n==1:
        return 1
    return n*2-1+addodd(n-1)
    
print(addodd(int(input("enter the no ==>> "))))