'''7. Write a python program to access a function inside a function.'''

def square30():
    for e in range(1,31):
        print(e**2,end=" ")
        
def display():
    print("square of nuber upto 30 ")
    square30() 
    
square30()