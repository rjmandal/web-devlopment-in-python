'''10. Write a recursive python function to print a number in reverse order.'''

def reverse(n):
    if n>0:
        print(n%10,end="")
        reverse(n//10)

reverse(int(input("enter a no ==>> ")))