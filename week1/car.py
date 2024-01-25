class Car:
    def __init__(self, make, model, current_speed, max_speed, fuel_level):
        self.make = make
        self.model = model
        self.current_speed = current_speed
        self.max_speed = max_speed
        self.fuel_level = fuel_level
    
    def accelerate(self, delta):
        if self.current_speed + delta > self.max_speed:
            delta = self.max_speed - self.current_speed

        self.current_speed += delta
        self.fuel_level -= delta

        if self.fuel_level <= 0:
            self.fuel_level = 0
            self.current_speed = 0
    
    def brake(self, delta):
        if self.current_speed - delta < 0:
            delta = self.current_speed

        self.current_speed -= delta
    
    def refuel(self, delta):
        if self.fuel_level + delta > 100:
            delta = 100 - self.fuel_level

        self.fuel_level += delta
