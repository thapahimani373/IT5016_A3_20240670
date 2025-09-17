class Vehicle:
    def move(self):
        print("Vehicle moves somehow")

class Car(Vehicle):
    def move(self):
        print("Car drives on road")  # Different action for the same method.

class Boat(Vehicle):
    def move(self):
        print("Boat sails on water")

def travel(vehicle):
    vehicle.move()  # Works for any vehicle – polymorphism!

# Analysis: Polymorphism is flexible – one travel() function handles all. It’s extendable; I could add Plane without changing travel(). I like how it makes code reusable across types.
car = Car()
boat = Boat()
travel(car)
travel(boat)
