'''5. Write a recursive python function to calculate sum of cubes of first N natural numbers '''

def addcube(n):
    if n==1:
        return 1
    return n**3 + addcube(n-1)
    
print(addcube(int(input("enter the no ==>> "))))