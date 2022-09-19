'''4. Write a python program to create a function that checks 
whether a passed string is palindrome or not.'''

def palindrome(s):
    l=len(s)//2
    i=0
    j=-1
    
    while l:
        if s[i]==s[j]:
            i+=1
            j-=1
        else:
            return False
        l-=1
    else:
        return True


print(palindrome(input("enter the string ==>> ")))
