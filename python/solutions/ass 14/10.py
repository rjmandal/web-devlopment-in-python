"""10. Write a python script to sort a list."""

n=int(input("enter n no you want to enter in a list==>> "))
l=[]
i=0
print("enter the ",n," no in a list")
while i<n:
    l.append(int(input()))
    i+=1
print("you enterd this list ==>> ",l)
# l=l.sort()
print(sorted(l))