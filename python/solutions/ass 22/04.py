'''4. Write a recursive python function to calculate sum of squares of first N natural
numbers'''

def SQUAREnatural(n):
    if n==1:
        return 1
    return n**2 + SQUAREnatural(n-1)
    
print(SQUAREnatural(int(input("enter the no ==>> "))))