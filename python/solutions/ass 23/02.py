'''2. Create a generator to produce first n odd natural numbers'''

def oddproducer(n):
    e=1
    while n:
        yield e
        e+=2
        n-=1

for e in oddproducer(int(input("enter the no ==>> "))):
    print(e,end=" ")

