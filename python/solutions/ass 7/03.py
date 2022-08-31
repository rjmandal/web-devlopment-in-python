while 1:    
    print("a.Check Isosceles Triangle or not")
    print("b.Check Right angled triangle or not")
    print("c.Equilateral triangle or not")
    print("d.Exit")
    match input("enter your choice from above ==>> "):
        case 'a':
            s1=int(input("enter the first side ==>> "))
            s2=int(input("enter the second side ==>> "))
            s3=int(input("enter the third side ==>> "))
            if s1==s2 or s1==s3 or s2==s3:
                print("result ==>> yes")
            else:
                print("result ==>> no")
        case 'b':
            s1=int(input("enter the H side ==>> "))
            s2=int(input("enter the B side ==>> "))
            s3=int(input("enter the P side ==>> "))
            if s1**2==s2**2 + s3**2 :
                print("result ==>> yes")
            else:
                print("result ==>> no")
        case 'c':
            s1=int(input("enter the first side ==>> "))
            s2=int(input("enter the second side ==>> "))
            s3=int(input("enter the third side ==>> "))
            if s1==s2==s3:
                print("result ==>> yes")
            else:
                print("result ==>> no")
        case 'd':
            exit(1)
        case _:
            print("enter valid choice ")