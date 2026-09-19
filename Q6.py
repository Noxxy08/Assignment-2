class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def describe(self):
        print(f"{self.brand} vehicle moving at {self.speed} km/h.")

    def sound(self):
        print("The vehicle makes a generic sound.")

class Car(Vehicle):
    def __init__(self, brand, speed, colour):
        super().__init__(brand, speed)
        self.colour = colour

    def sound(self):
        print(f"{self.brand} car goes Vroom Vroom!")

    def describe(self):
        super().describe()
        print(f"Shade is {self.colour} colour.")


class Bike(Vehicle):
    def __init__(self, brand, speed, has_brakes):
        super().__init__(brand, speed)
        self.has_brakes = has_brakes

    def sound(self):
        print(f"{self.brand} bike goes Brrr Brrr!")

    def describe(self):
        super().describe()
        brakes_info = "has brakes" if self.has_brakes else "single-speed"
        print(f"It {brakes_info}.")

vehicle = Vehicle("Generic", 60)
vehicle.describe()
vehicle.sound()

print()

car = Car("Toyota", speed:=120, colour:= "red")
car.describe()
car.sound()

print()

bike = Bike("Trek", 25, True)
bike.describe()
bike.sound()

print()

# Polymorphism: treat all objects through the same interface
print("Looping through different vehicle types:")
vehicles = [vehicle, car, bike]
for v in vehicles:
    v.sound()