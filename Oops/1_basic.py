class Car:
    def __init__(self,make,year):
        self.make = make
        self.year = year
    def display_info(self):
        print(f"This car is a {self.year} {self.make}.")

my_car = Car("Toyoto",2006)
my_car.display_info()
