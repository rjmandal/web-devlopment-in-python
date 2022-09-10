'''5. Write a python program to check if all items in the tuple are the same.'''

t=tuple([int(e) for e in input('enter the no seperated by comma ==>> ').split(',')])
print("enterd tuple is ==>>",t)
i=0
for e in t:
    if e==t[-i]:
        i+=1
    else:
        print("no")
        break
else:
    print("yes")