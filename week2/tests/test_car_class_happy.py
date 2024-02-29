import pytest
from car import Car

class TestCarClassHappy:

    def test_new_car(self):
        car1 = Car("Honda", "Civic", 100, 130, 100)

        assert car1.make == "Honda"
        assert car1.model == "Civic"
        assert car1.current_speed == 100
        assert car1.max_speed == 130
        assert car1.fuel_level == 100

# accelerate method tests
    def test_accelerate_fuel_change(self):
        car1 = Car("Honda", "Civic", 100, 130, 100)
        car1.accelerate(5)

        assert car1.fuel_level == 95
    
    def test_accelerate_speed_change(self):
        car1 = Car("Honda", "Civic", 100, 130, 100)
        car1.accelerate(5)

        assert car1.current_speed == 105
    
    def test_accelerate_speed_bounds(self):
        car1 = Car("Honda", "Civic", 129, 130, 50)
        car1.accelerate(2)

        assert car1.current_speed == 130
        assert car1.fuel_level == 49
    
    def test_accelerate_fuel_bounds(self):
        car1 = Car("Honda", "Civic", 70, 130, 5)
        car1.accelerate(10)

        assert car1.fuel_level == 0
        assert car1.current_speed == 75

# brake method tests
    def test_brake_speed_change(self):
        car1 = Car("Honda", "Civic", 100, 130, 100)
        car1.brake(5)

        assert car1.current_speed == 95
    
    def test_brake_speed_bounds(self):
        car1 = Car("Honda", "Civic", 7, 130, 100)
        car1.brake(10)

        assert car1.current_speed == 0

# refuel method tests
    def test_refuel_fuel_change(self):
        car1 = Car("Honda", "Civic", 100, 130, 50)
        car1.refuel(10)

        assert car1.fuel_level == 60
    
    def test_refuel_fuel_bounds(self):
        car1 = Car("Honda", "Civic", 100, 130, 99)
        car1.refuel(10)
        
        assert car1.fuel_level == 100
    