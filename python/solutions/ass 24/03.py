'''3. Write a python program to create 2 objects of the user class and assign different
values.'''

class User:
    def __init__(self,name):
        self.name=name
              
u1=User(input("enter name ==>> "))
u2=User(input("enter name ==>> "))
print("User 1 ==>> ",u1.name)
print("User 2 ==>> ",u2.name)