class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        full_name = f"{self.make} {self.model} {self.year}"
        return full_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles it!")

    def update_odometer(self, mile):
        if mile >= self.odometer_reading:
            self.odometer_reading = mile
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, incres_miles):
        self.odometer_reading += incres_miles


class Battery:
    def __init__(self, battery_size=100):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This is a {self.battery_size} --KWh battery.")

    def get_range(self):
        range = self.battery_size * 3
        print(f"This car can go about {range} miles on a full charge!")

    def update_battery(self):
        if self.battery_size < 150:
            self.battery_size = 150
            print(f"We have update your battery now its a {self.battery_size} --KWh battery now! ")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.update_battery()
my_tesla.battery.get_range()
