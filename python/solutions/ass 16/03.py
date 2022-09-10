'''3. Write a python program to reverse the tuple'''

t=tuple([int(e) for e in input("enter the value seperated by comma ==>> ").split(',')])
print("your enterd this tuple ==>> ",t)
print(t[::-1])