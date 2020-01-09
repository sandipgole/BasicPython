class A:
    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

class B:
    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")

class C(A,B):
    pass

c1=C()
c1.feature3()
