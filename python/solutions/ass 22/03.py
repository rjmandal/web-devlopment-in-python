'''3. Write a recursive python function to calculate sum of first N even natural numbers'''

def addeven(n):
    if n==1:
        return 2
    return n*2 + addeven(n-1)
    
print(addeven(int(input("enter the no ==>> "))))