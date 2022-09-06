n=int(input("enter the no ==>> "))
r=range(2,n)
for e in r:
    if n%e==0:
        print("not a prime no")
        break
else:
    print("prime no")