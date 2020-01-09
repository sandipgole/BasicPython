class students:
    def __init__(self):
        self.age=19
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False

ram=students()
hari=students()
hari.age=20
if ram.compare(hari):
    print("They are same")
else:
    print("They are different")

class Teacher:
    def __init__(self):
        self.name='ram'
        self.age=50
        self.subject='python'
    def show(self):
        print(self.name)
        print(self.age)
        print(self.subject)
Rameshwor=Teacher()
Rameshwor.show()


