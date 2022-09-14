class Car():
    """A simple class to describe a car"""
    def __init__(self,make,model,year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odomter_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name

    def read_odometer(self):
        """Prints out the odometer reading of a vehicle"""
        print(f"This car has {self.odomter_reading} miles on it.")

my_car = Car('Audi', 'S3','2019')
print(my_car.get_descriptive_name())
my_car.read_odometer()
my_car.odomter_reading = 33
my_car.read_odometer()