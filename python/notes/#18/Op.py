
a = 5
b = 6
c = "Navin"
d = " Reddy"
# print(a + b)    
# print(int.__add__(a,b))
# print(c + d)
# print(str.__add__(c,d))






class Student:
    def __init__(self, m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
        total_m1 = self.m1 + other.m1
        total_m2 = self.m2 + other.m2
        s3 = Student(total_m1,total_m2)
        return s3


    def __str__(self):
        return str(self.m1) + " : " +  str(self.m2)    

s1 = Student(45,34)
s2 = Student(99,77)  

s3 = s1 + s2    # Student.__add__(s1,s2)
                # s1.__add__(s2)


print(a)
print(s3)