class A:
    def __init__(self):
        print("in init A")

    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

class B:
    def __init__(self):
        print("In init B")


    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")
class C(B,A):
    def __init__(self):
        super().__init__()
        print("in init c")

obj=C()


