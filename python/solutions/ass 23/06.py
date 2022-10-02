'''6. Create a generator to produce first n prime numbers'''

def primeproducer(n):
    
    no=2
    c=0
    while True:
        for e in range(2,no):
            if no%e==0:
                break
        else:
            c+=1
            yield no
            if c==n:
                break
        no+=1
                           
# for e in primeproducer(int(input("enter the no ==>> "))):
#     print(e,end=" ")

l1=[e for e in primeproducer(int(input("enter the no ==>> ")))]
print(l1)

