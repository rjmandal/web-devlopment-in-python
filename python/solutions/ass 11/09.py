n=int(input("enter the decimal number ==>> ")) c
while n:
    r=n%10   
    n=n//10
    sum=sum+r
print(sum)