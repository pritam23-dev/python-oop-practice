# Polymorphism # eti holo = একজন বেক্তির আলাদা আলাদা ক্যারেক্টার এ কাজ করা 
# like =  men ➡️son , husband , father

class Vehicle:
    def __init__(self, Model,Brand,Component):
        self.Model = Model
        self.Brand = Brand
        self.Component = Component

class plane(Vehicle):
    pass

class car(Vehicle):
    pass

class bike(Vehicle):
    pass

p1 = plane("pritam420","pritam","All component")

c1 = car("BMW","m4","Main component")

b1 = bike("gyxser","R15","All component")

print(p1.Model, p1.Component)

print(c1.Brand)

print(b1.Model, b1.Brand, b1.Component)



