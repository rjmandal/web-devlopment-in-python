'''6. Write a recursive python function to calculate the factorial of a number.'''

def addfact(n):
    if n==1:
        return 1
    return n * addfact(n-1)
    
print(addfact(int(input("enter the no ==>> "))))