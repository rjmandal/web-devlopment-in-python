'''5. Write a python program to delete the age property of the user.'''

class User:
    
    def __init__(self):
        self.age = 22
        self.course="bca"
        
u1 = User()
u2 = User()
del(u1.age)
print("course = ",u1.course)
# print("age = ",u1.age)