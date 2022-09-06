# 2. Write a Python script to create a list of first N odd natural numbers.

n=int(input("enter n no ==>> "))
l=[x*2+1 for x in range(n)]
print(l)