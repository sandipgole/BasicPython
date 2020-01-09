class Student:


    def __init__(self,name,roll,grade):
        self.name=name
        self.roll=roll
        self.grade=grade


    def info(self):
        print("Name: "+self.name)
        print("Roll_no. "+self.roll)
        print("grade: "+self.grade)


Rohan=Student('Rohan','1','10th')
Rohan.info()