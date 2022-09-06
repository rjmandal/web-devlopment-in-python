r1=range(1,100)
for n in r1:
    r2=range(2,n)
    for e in r2:
        if n%e==0:
            break
    else:
        print(n)