n=int(input("enter the decimal number ==>> "))
ans=0
i=0
while n:
    r=n%8   
    n=n//8
    ans=r*10**i+ans
    i+=1
print(ans)
    