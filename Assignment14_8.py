class Vehicle:
    def start(self):
        print("Vehicle starts...")

class Car(Vehicle):
    def start(self):
        print("Car starts...")

v = Vehicle()
v.start()

c = Car()
c.start()