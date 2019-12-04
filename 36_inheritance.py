class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def Bark(self):
        print(" Dog Barks")



class Cat(Mammal):
    def Myoi(self):
        print(" cat meo")


dog1=Dog()
dog1.walk()
dog1.Bark()
cat1=Cat()
cat1.Myoi()

