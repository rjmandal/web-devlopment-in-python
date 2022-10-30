'''4. Write a python program to init default values for user object using __init__ method.'''

class User:
    
    def __init__(self):
        self.school="sd bihani"
        self.course="bca"
        
u1 = User()
u2 = User()

print("school = ",u1.school)
print("course = ",u1.course)