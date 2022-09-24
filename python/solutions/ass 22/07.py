'''7. Write a recursive python function to calculate sum of the digits of a given number.'''

def adddigit(n):
    if n>0:
        return n%10 + adddigit(n//10)
    else:
        return 0
    
print(adddigit(int(input("enter the no ==>> "))))