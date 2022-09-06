"""10. Write a Python script to create a list, where each element of 
the list is a digit of a given number."""


n=int(input("enter the no of digits you want to enter ==>> "))
l1=[]
i=0
print("enter ",n," digit")
while i<n:
    l1.append(int(input()))
    i+=1
print("list = ",l1)


# altrnate option


# l1=[]
# l1=eval(input("enter digits ==>> "))
# print(l1)