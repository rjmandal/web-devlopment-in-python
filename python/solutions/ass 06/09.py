year=int(input("enter a year ==>> "))
print("leap year" if year%400==0 or year%100!=0 and year%4==0 else "not a leap year")