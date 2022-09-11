'''2. Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division'''


while 1:    
 print("1.Addtion\n2.Subtration\n3.Multiplication\n4.Division\n5.exit\n")
 match int(input("enter your choice ==>> ")):
    case 1:
        print("result ==>> ",int(input("enter first no ==>> "))+int(input("enter second no ==>> ")),"\n")
    case 2:
        print("result ==>> ",int(input("enter first no ==>> "))-int(input("enter second no ==>> ")),"\n")
    case 3:
        print("result ==>> ",int(input("enter first no ==>> "))*int(input("enter second no ==>> ")),"\n")
    case 4:
        print("result ==>> ",int(input("enter first no ==>> "))/int(input("enter second no ==>> ")),"\n")
    case 5:
        exit(1)
    case _:
        print("enter a valid choice")