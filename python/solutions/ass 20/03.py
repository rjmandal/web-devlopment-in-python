'''3. Write a python program to create a function that prints 
the even numbers from a given list. 
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]'''

def even(l):
    list=[]
    for e in l:
        if e %2 ==0:
            # list.append(e)
            print(e,end=" ")
    print()

List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even(List)


