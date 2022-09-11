'''5. Write a program which takes a number from user. Print Saurabh Shukla if the
number is even, print Prateek Jain if the number is negative odd number and print 
Aditya Choudhary if number is positive odd number.'''


no=int(input("enter any no ==>> "))
match no:
    case no if no%2==0:
        print("sourabh sukla")
    case no if no<0 and no%2!=0:
         print("Prateek Jain") 
    case no if no>0 and no%2!=0:
        print("Aditya Choudhary")