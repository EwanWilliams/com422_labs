from car import Car

def run():
    cars = []
    cars.append(Car("Nissan", "180SX", 50, 137, 30))
    cars.append(Car("Honda", "Civic", 30, 110, 63))
    cars.append(Car("Mazda", "Miata", 0, 130, 15))

    for vehicle in cars:
        print(f"Vehicle: {vehicle.make} {vehicle.model} | {vehicle.current_speed}/{vehicle.max_speed}mph | Fuel: {vehicle.fuel_level}%")
    
    cars[0].accelerate(100)
    cars[1].brake(35)
    cars[2].refuel(100)
    print()

    for vehicle in cars:
        print(f"Vehicle: {vehicle.make} {vehicle.model} | {vehicle.current_speed}/{vehicle.max_speed}mph | Fuel: {vehicle.fuel_level}%")

if __name__ == "__main__":
    run()
    