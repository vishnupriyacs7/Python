# Object oriented programming
# ================================

class Cars :
    def __init__(self,name,price,color):
        self.name = name
        self.price = price
        self.color = color

    def start(self):
        print(self.name + " Engine started")

car1 = Cars("Maruti Swift",100000, "Red")
car2 = Cars("Toyota Innova",200000, "White")

car1.price = 150000
car2.color = "blue"

# del car1.color
# del car2
print(car1.name, car1.price, car1.color)
print(car2.name, car2.price, car2.color)

car1.start()
car2.start()
