'''2. Create a generator to produce first n odd natural numbers'''

def generator(n):
    while n:
        yield e*2-1
        n-=1

print(generator(int(input("enter the no ==>> "))))

