from carpark import Carpark

class Tui:

    @staticmethod
    def get_new_reg():
        new_reg = input("Enter car registration: ")
        return new_reg
    
    @staticmethod
    def alert_error(error):
        print(f"ERROR: {error}")
    
    @staticmethod
    def display_carpark_status(carpark):
        space_overview = "| "
        spaces_free = 0

        for space in carpark.spaces:
            if space == None:
                spaces_free += 1
            else:
                space_overview += f"{space.reg} | "
        
        print(f"{space_overview}& {spaces_free} free spaces.")