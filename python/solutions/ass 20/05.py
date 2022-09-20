'''5. Write a python program to create a function to find the Min of three numbers.'''

def mof3(a,b,c):
    print((a if a>c else c) if a>b else (b if b>c else c))
    
print("enter any three no to find greatest among them")
mof3(int(input("enter first number ==>> ")),int(input("enter second number ==>> ")),int(input("enter third number ==>> ")))