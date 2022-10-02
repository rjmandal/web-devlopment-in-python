'''8. Create an endless iterator using generator method to produce Prime numbers'''

def primeproducer():
    no=2
    while True:
        for e in range(2,no):
            if no%e==0:
                break
        else:
            yield no
        no+=1
                        
it =primeproducer()
list=[]
while True:
    ans=input("enter [y/n] ==>> ")
    if ans =="y":
        e=next(it)
        print(e)
        list.append(e)
    else:
        break
print(list)