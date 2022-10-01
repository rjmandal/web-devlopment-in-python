'''5. Create a generator to produce first n terms of Fibonacci series'''

def fibonacciproducer(n):
    a,b=0,1
    while n:
        yield a
        a,b=b,a+b
        n-=1

for e in fibonacciproducer(int(input("enter the no ==>> "))):
    print(e,end=" ")

