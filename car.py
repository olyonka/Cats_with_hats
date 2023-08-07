class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed = max(0, self.speed - 5)

    def display_speed(self):
        print(f"Current speed: {self.speed} km/h")


# Example usage
car = Car('Toyota', 'Camry', 2022)

car.accelerate()
car.display_speed()  # Output: Current speed: 5 km/h

car.accelerate()
car.display_speed()  # Output: Current speed: 10 km/h

car.brake()
car.display_speed()  # Output: Current speed: 5 km/h

car.brake()
car.display_speed()  # Output: Current speed: 0 km/h