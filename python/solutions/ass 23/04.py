'''4. Create a generator to produce squares of first N natural numbers'''

def squareproducer(n):
    e=1
    while n:
        yield e**2
        e+=1
        n-=1

for e in squareproducer(int(input("enter the no ==>> "))):
    print(e,end=" ")

