n1=int(input("enter no1 ==>> "))
n2=int(input("enter no2 ==>> "))
if n1>n2:
    n1=n1+n2
    n2=n1-n2
    n1=n1-n2
r=range(n2,n1*n2+1)
for e in r:
    if e%n1==0 and e%n2==0:
        print(e)
        break