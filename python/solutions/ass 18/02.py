'''2. Write a python program to access the items of a dictionary by referring to its key
name.'''



d=dict(name="Sanjay mandal",age=23,gender="male",language1="Python",
       language2="C",language3="English",occupation="BCA")

# print(d["name"])
for e in d:
    print(e,"  ==>>  ",d[e])