'''10. Write a recursive python function to find the Nth term of the Fibonacci series.'''
    
def Fibonacci(n):
    a,b=-1,1
    if n>0:
        Fibonacci(n-1)
        a=b
        b=a+b
    return b

print(Fibonacci(int(input("enter the no ==>> "))))