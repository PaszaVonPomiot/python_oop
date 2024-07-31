"""
Write a class that will fit the usage shown below
"""


class Car:
    ...


car = Car(brand="Skoda", color="green")
print(car.mileage)  # should be 0 initially
car.drive(kilometers=100)

print(f"My {car.brand} is {car.color} and drove for {car.mileage}")
