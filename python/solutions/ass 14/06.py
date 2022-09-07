'''6. Write a Python script to calculate the sum of elements in a given list of numbers.'''

n=int(input("enter n no you want to enter in a list==>> "))
l=[]
i=0
print("enter the ",n," no in a list")
while i<n:
    l.append(int(input()))
    i+=1
print("you enterd this list ==>> ",l)
print("sum of the no in this list ==>> ",sum(l))
