'''4. Write a Python script to find if “Python” is present in the set thisset = {"Java",
"Python", "Django"}'''

thisset = {"Java","Python", "Django"}
for e in thisset:
    if e=="Python":
        print("yes")
        break
else:
    print("no")