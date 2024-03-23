from car import Car

class Carpark:

    def __init__(self, size):
        self.size = size
        self.spaces = [None]*size
    

    def add_car(self, new_car):
        for i in range(self.size):
            if self.spaces[i] == None:
                self.spaces[i] = new_car
                return True
        
        return False
    

    def remove_car(self, to_remove):
        for i in range(self.size):
            if self.spaces[i] == None:
                continue
            elif self.spaces[i].reg == to_remove:
                self.spaces[i] = None
                return True
            
        return False
    

    def spaces_taken_free(self):
        taken = 0
        for space in self.spaces:
            if space != None:
                taken += 1
        
        return (taken, self.size-taken)
    