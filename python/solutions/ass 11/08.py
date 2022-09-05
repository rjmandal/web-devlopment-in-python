n=int(input("enter the number ==>> "))
sum=0
while n:
    r=n%10   
    n=n//10
    sum=sum+r
print(sum)