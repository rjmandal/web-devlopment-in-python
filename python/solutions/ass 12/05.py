n=int(input("enter no ==>> "))
while 1:
    n+=1
    r2=range(2,n)
    for e in r2:
        if n%e==0:
            break
    else:
        print(n)
        break