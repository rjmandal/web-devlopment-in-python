n=int(input("enter the decimal number ==>> "))
ans=0
i=0
while n:
    r=n%2   
    n=n//2
    ans=r*10**i+ans
    i+=1
print(ans)
    