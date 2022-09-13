'''9. Write a python program to merge two python dictionaries into one dictionary.'''


d1={"name":"Sanjay mandal","age":23}
d2={"gender":"male","language1":"Python","language2":"C"}
for e in d2:
    d1[e]=d2[e]
print(d1)