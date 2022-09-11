'''10. Write a program to display day name on the basis of user’s liking of a colour. 
Ask user for his favorite colour. User can answer in a sentence like “I like red 
colour”. Assuming all colour name entered by user is in lowercase. Use match case to 
display day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday'''


s=input("enter your favourite colour in lowercase like i like _____ colour ==>> ")
match s:
    case s if "yellow" in s:
        print("Monday")
    case s if "blue" in s:
        print("Tuesday")
    case s if "orange" in s:
        print("Wednesday")
    case s if "white" in s:
        print("Thursday")
    case s if "black" in s:
        print("Friday")
    case s if "red" in s:
        print("Saturday")
    case _:
        print("red the instruction carefully")