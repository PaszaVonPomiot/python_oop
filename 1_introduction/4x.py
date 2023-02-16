"""
Write a class that will fit the usage shown below
"""


class Car:
    ...


car = Car(brand="Skoda", color="red")
car.print_mileage()  # should be 0
car.drive(kilometers=100)

print(f"My {car.brand} is {car.color} and drove for {car.mileage}")
