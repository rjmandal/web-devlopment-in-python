'''9. Write a recursive python function to print octal of a given decimal number'''
    
def octaldec(n):
    i=0
    if n>0:
        return octaldec(n//8)*10**(i+1)+n%8
    else:
        return 0

print(octaldec(int(input("enter the no ==>> "))))