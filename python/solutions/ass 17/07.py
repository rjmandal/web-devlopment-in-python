'''7. Write a python program to remove last item of the given set
thisset = {"Python", "Django", "JavaScript", “SQL”}'''


thisset = {"Python", "Django", "JavaScript",'SQL'}
print(thisset)
print("one item removed ==>> ",end=" ")
thisset.remove("SQL")
print(thisset)
print("poped item ==>> ",thisset.pop())
print(thisset)