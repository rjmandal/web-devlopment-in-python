month=int(input("enter the month no ==>> "))
if month%2==0:
    print("30")
elif month==2:
    print("28 or 29")
elif month%2==0:
    print("31")
else:
    print("enter valid input")