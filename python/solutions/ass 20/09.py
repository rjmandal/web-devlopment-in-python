'''9. Write a python program to create a function to check whether a string is a pangram
or not.'''

def pangram(s):
    l=97
    u=65
    for e in range(1,26):
        if chr(l) in s or chr(u) in s:
            l+=1
            u+=1
        else:
            return False
    else:
        return True           
        

print(pangram(input("enter the string ==> ")))