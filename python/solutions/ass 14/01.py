# 1. Write a Python script to create a list of first N natural numbers.

n=int(input("enter n no ==>> "))
l=[x+1 for x in range(n)]
print(l)