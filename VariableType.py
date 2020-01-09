class Mycar:
    no_of_wheel=4 #static variable

    def __init__(self):
        self.mil=40    #instance variable
        self.com='Audi'

AudiA3=Mycar()
print(AudiA3.mil)
print(AudiA3.com)
Mycar.no_of_wheel=10
print(Mycar.no_of_wheel)