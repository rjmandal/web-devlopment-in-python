n=int(input("enter no ==>> "))
i=0
p=0
while 1:
    i+=1
    r=range(2,i)
    for e in r:
        if i%e==0:
            break
    else:
        print(i)
        p+=1
        if p==n:
            break