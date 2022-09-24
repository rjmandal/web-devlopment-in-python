'''8. Write a recursive python function to print binary of a given decimal number.'''

# def binarydec(n):
#     if n>0:
#         binarydec(n//2)
#         print(n%2,end="") 
    
# binarydec(int(input("enter the no ==>> ")))


    # """ alternate method """
    
def binarydec(n):
    i=0
    if n>0:
        return binarydec(n//2)*10**(i+1)+n%2
    else:
        return 0

print(binarydec(int(input("enter the no ==>> "))))