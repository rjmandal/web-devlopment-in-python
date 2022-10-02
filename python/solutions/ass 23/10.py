'''10. Define a function which calculates HCF of two numbers. Define and apply a
decorator to check whether two given numbers are co-prime or not.'''

def hcf_dec(hcf):
    def newhcf(n1,n2): 
        h=hcf(n1,n2)
        print(h)
        print("co - prime no" if h==1 else "not a co prime")
    return newhcf
            
@hcf_dec
def hcf(n1,n2):
    if n1>n2:
        n1,n2=n2,n1
    n=n1+1
    for e in range(1,n):
        if n1%e==0 and n2%e==0:
            hcf=e
    return hcf
    
hcf(int(input("enter first no ==>> ")),int(input("enter second no ==>> ")))
     