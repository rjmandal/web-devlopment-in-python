# 7. Write a python program to Print all items by referring to their index number (thislist =
# ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]


thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
for e in thislist:
    print(thislist.index(e),e,sep=' = ')