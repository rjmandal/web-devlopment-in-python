n1=int(input("enter no1 ==>> "))
n2=int(input("enter no2 ==>> "))
if n1>n2:
    n1=n1+n2
    n2=n1-n2
    n1=n1-n2
r=range(2,n1+1)
for e in r:
    if n1%e==0 and n2%e==0:
        print("not a co prime no ")
        break
else:
    print("co prime no ")   