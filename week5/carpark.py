from car import Car

class Carpark:

    def __init__(self, size):
        self.size = size
        self.spaces = [None]*size
    

    def add_car(self, new_car):
        for i in range(len(self.spaces)):
            if self.spaces[i] == None:
                self.spaces[i] = new_car
                return True
        
        return False
    
    def remove_car(self, to_remove):
        for i in range(len(self.spaces)):
            if self.spaces[i] == None:
                continue
            elif self.spaces[i].reg == to_remove:
                self.spaces[i] = None
                return True
            
        return False