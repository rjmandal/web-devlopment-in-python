'''7. Write a python program to check whether a given number is positive, negative or
zero using match case statement'''


n = int(input("enter a no ==>>  "))
match n:
    case n if n>0:
        print("positive")
    case n if n<0:
        print("negative")
    case n if n==0:
        print("zero")
    case _:
        print("enter a valid no")