'''2. Write a python program to create a function that takes a
 number as a parameter and checks if the number is prime or not.'''


def prime(no):
    for e in range(2,n):
        if no%e==0:
            return False
            break
    else:
        return True

n=int(input("enter the no ==>> "))
print(prime(n))