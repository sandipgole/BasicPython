class Pycharm:
    def execute(self):
        print("compiling")
        print("running")
class GoleEditor:
    def execute(self):
        print("checking")
        print("compilling")
        print("running")

class Laptop:
    def code(self,ide):
        ide.execute()

ide=GoleEditor()
Acer=Laptop()
Acer.code(ide)