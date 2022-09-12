'''1. Write a python program to store all the programming languages known to you using
Set.'''

set={"Python","c","c++","java","javascript","R","B","BCPL","PHP"}
print(set,type(set),sep="\n")

set1={e for e in input("enter the programming languages you know seperated by comma==>> ").split(",")}
print(set1,type(set1),sep="\n")

for e in set:
    print(e,end="  ")