'''1. Write a python program to create a user class with 3 properties : name, age, email.'''

class User:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
    def show(self):
        print(self.name)
        print(self.age)
        print(self.email)
              
u1=User(input("enter name ==>> "),eval(input("enter age ==>> ")),input("enter email ==>> "))
u1.show()