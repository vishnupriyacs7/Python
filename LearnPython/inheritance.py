# parent class
class Person:
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact

    def address(self):
        print(self.name,self.contact)

# child class
class Doctor(Person):
    pass #add pass if not ppty or methods never be empty

class Patient(Person):
    pass

doc1 = Doctor("vishnu",12345)
pat1 = Patient("Abhi",98765)

doc1.address()
pat1.address()
