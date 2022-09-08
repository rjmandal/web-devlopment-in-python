'''9. Write a Python script to print indices of all 
    occurrences of a given element in a given list.'''
    
n=int(input("enter no of element you want to enter in a list==>> "))
l=[]
i=0
print("enter the ",n," elements in a list")
while i<n:
    l.append(eval(input()))
    i+=1
print("you enterd this list ==>> ",l)
element=eval(input("enter the element you want to print indice ==>> "))
l1=[]
j=0
for e in l:
    if element==e:
        l1.append(j)
    j+=1
print(element," = ",l1)