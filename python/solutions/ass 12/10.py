n1=int(input("enter no1 ==>> "))
n2=int(input("enter no2 ==>> "))
if n1>n2:
    n1=n1+n2
    n2=n1-n2
    n1=n1-n2
r=range(1,n1)
for e in r:
    if n1%e==0 and n2%e==0:
        hcf=e
print(hcf)