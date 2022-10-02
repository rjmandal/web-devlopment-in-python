'''9. Define a function which takes lengths of three sides of a triangle as arguments and
display the perimeter or triangle. Define and apply a decorator which checks for the
validity of the triangle on the basis of lengths of the side. This makes the perimeter to
be displayed when the triangle can exist with the given lengths of the sides.'''

def tri_dec(tri):
    def newTri(s1,s2,s3):
        tri(s1,s2,s3) if s1+s2>s3 and s1+s3>s2 and s2+s3>s1 else print("not a valid triangle")
    return newTri
            
@tri_dec
def tri(s1,s2,s3):
    print("perimeter of trinagle ==>> ",s1+s2+s3)
    
tri(int(input("enter first side ==>> ")),int(input("enter second side ==>> ")),int(input("enter third side ==>> ")))
     