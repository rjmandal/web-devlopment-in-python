n1=int(input("enter no1 ==>> "))
n2=int(input("enter no2 ==>> "))
if n1>n2:
    n1=n1+n2
    n2=n1-n2
    n1=n1-n2
r1=range(n1,n2+1)
for n1 in r1:
    r2=range(2,n1)
    for e in r2:
        if n1%e==0:
            break
    else:
        print(n1)