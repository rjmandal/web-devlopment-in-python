no1,no2,no3 = int(input("enter the no1 ==>> ")),int(input("enter the no2 ==>> ")),int(input("enter the no3 ==>> "))
print((no1 if no1>no3 else no3) if no1>no2 else (no2 if no2>no3 else no3))
        