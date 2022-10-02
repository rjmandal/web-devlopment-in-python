'''7. Create an endless iterator using generator method to produce terms of Fibonacci
series'''

def fibonacciproducer():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

it=fibonacciproducer()
list=[]
while True:
    ans=input("select [y/n] ==>> ")
    if ans=="y":
        e=next(it)
        print(e)
        list.append(e)
    else:
        break    
print(list)
    