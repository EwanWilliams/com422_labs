import pytest
from car import Car

class TestCarClassSad:

    def test_new_car_fuel_in_range(self):
        car1 = Car("Honda", "Civic", 100, 130, 101)
        