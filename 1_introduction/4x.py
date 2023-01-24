"""
Write a class that will fit to usage shown below
"""


class Car:
    ...


car = Car(brand="skoda", color="red")
car.print_mileage()  # should be 0
car.drive(kilometers=100)
car.print_mileage()  # should be 10
