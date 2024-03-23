from tui import Tui
from carpark import Carpark
from car import Car


def run():
    carpark = Carpark(15)

    while 1:
        Tui.display_carpark_status(carpark)

        input()
    

if __name__ == "__main__":
    run()