a,b,c=int(input("enter a ==>> ")),int(input("enter b ==>> ")),int(input("enter c ==>> "))
d=b-4*a*c
if(d>0):
    print("roots are real and distinct")
elif(d==0):
    print("roots are real and equal")
else:
    print("roots are imaginary")
