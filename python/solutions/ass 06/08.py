a=int(input("enter a ==>> "))
b=int(input("enter b ==>> "))
c=int(input("enter c ==>> "))
d=b-4*a*c
if(d>0):
    print("roots are real and distinct")
elif(d==0):
    print("roots are real and equal")
else:
    print("roots are imaginary")
