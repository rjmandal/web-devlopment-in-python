# 9. Write a Python script to create a list of city names taken from the user.

n=int(input("enter the no of city names you want to enter ==>> "))
l1=[]
i=0
print("enter ",n," city names")
while i<n:
    l1.append(input())
    i+=1
print(l1)

# altrnate option

# l1=[]
# l1=eval(input("enter city names ==>> "))
# print(l1)