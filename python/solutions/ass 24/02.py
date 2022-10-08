'''2. Write a python program to create a user class with a method to greet the user.'''

class User:
    def greet(self,name):
        print("Hello",name)
              
u1=User()
u2=User()
u1.greet(input("enter name ==>> "))
u2.greet(input("enter name ==>> "))