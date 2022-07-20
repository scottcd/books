from car import Car 

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self, amount_of_gas):
        """Electric cars don't have gas tanks."""
        print("Electric cars don't have gas tanks.")





my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
