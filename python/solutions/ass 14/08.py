'''8. Write a Python script to print distinct elements 
along with their frequencies of occurrence in the list.'''

l=["sanjay",23,199,"sanjay",3+4j,True,23,True,True]
n=len(l)
i=0
while i<n-1:
    j=i+1
    count=1
    while j<n:
        if l[i]==l[j]:
            count+=1
            del(l[j])
            n-=1
        else:
            j+=1
    print(l[i],count,sep=" = ")
    i+=1