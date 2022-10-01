'''3. Create a generator to produce first n even natural numbers'''

def evenproducer(n):
    e=2
    while n:
        yield e
        e+=2
        n-=1

for e in evenproducer(int(input("enter the no ==>> "))):
    print(e,end=" ")

