'''4. Write a python program to Swap two tuples in Python.'''

t1=tuple([eval(e) for e in input("enter the vlaues seperated by comma ==>> ").split(',')])
t2=tuple([eval(e) for e in input("enter the vlaues seperated by comma ==>> ").split(',')])
print("you entered this tuple ","t1 ==>> ",t1,"t2 ==>> ",t2,sep="\n")
t1,t2=t2,t1
print()
print("swaped tuple","t1 ==>> ",t1,"t2 ==>> ",t2,sep="\n")
