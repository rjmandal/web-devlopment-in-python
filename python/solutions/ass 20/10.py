'''10. Write a python program to create a function to check whether a string is an anagram
or not.'''

def anagram(s1,s2):
    if len(s1)!=len(s2):
        sp1=s1.count(" ")+s1.count("'")
        sp2=s2.count(" ")+s2.count("'")
        l1=len(s1)-sp1
        l2=len(s2)-sp2
        if l1!=l2:
            return False
        
    for e in s1:
        if e.lower() not in s2 or e.upper() not in s2:
            return True
    else:
        return False
        
print(anagram(input("enter the first string ==> "),input("enter the second string ==>> ")))