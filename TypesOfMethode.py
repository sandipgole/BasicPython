class Student:
    university="gole university"

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def avg(self):
        return (self.m1+self.m2)/2


    @classmethod
    def getSchool(cls):
        return cls.university


    @staticmethod
    def info():
        print("This is static content")


s1=Student(20,60)
s2=Student(30,40)
print(s1.avg())
print((s2.avg()))
print(Student.getSchool())
Student.info()
