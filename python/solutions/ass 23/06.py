'''6. Create a generator to produce first n prime numbers'''

def primeproducer(n):
    a,b=0,1
    while n:
        yield a
        a,b=b,a+b
        n-=1

for e in primeproducer(int(input("enter the no ==>> "))):
    print(e,end=" ")

