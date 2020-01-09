class Student:

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.Laptop()
        self.moreinfo=self.additionalinfo()


    def show(self):
        print(self.name,self.roll)
        self.lap.show()
        self.moreinfo.showAddtionalinfo()

    class Laptop:

        def __init__(self):
            self.brand='Acer'
            self.cpu='intel'
            self.ram='8 gb ram'

        def show(self):
            print(self.brand,self.cpu,self.ram)

    class additionalinfo:

        def __init__(self):
            self.professionalclass='python'
            self.address='makawanpur'
            self.attitude='positive'

        def showAddtionalinfo(self):
            print(self.professionalclass,self.address,self.attitude)



Ram=Student('Ram',1)
Hari=Student('Hari',2)
Hari.show()
Ram.show()

