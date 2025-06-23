# Base Car class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"

# Battery class with upgrade method
class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range_km = 260
        elif self.battery_size == 100:
            range_km = 315
        print(f"This car can go about {range_km} km on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
            print("Battery upgraded to 100 kWh.")
        else:
            print("Battery is already at maximum capacity.")

# ElectricCar class
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

# Create instance and test upgrade
my_tesla = ElectricCar('tesla', 'model s', 2024)

print(my_tesla.get_description())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Upgrade battery and check again
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()