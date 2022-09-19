'''1. Write a python program to create a function that takes 
a list and returns a new list with the original list's 
unique elements.'''


def create(lf):
    n=len(lf)
    i=0
    while i<n-1:
        j=i+1
        while j<n:
            if lf[i]==lf[j]:
                del(lf[j])
                n-=1
            else:
                j+=1
        i+=1
    return lf

la=create([ eval(e) for e in input("enter the list no seperatd by comma ==>> ").split(",")])
print(la)