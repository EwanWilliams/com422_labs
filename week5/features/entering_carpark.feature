Feature: Vehicles entering the carpark

    Scenario: The carpark is empty and a car enters
        Given an empty carpark
        When a car with number plate "HT12 GFS" enters the carpark
        Then a car with number plate "HT12 GFS" occupies a space in the carpark
    
    Scenario: The carpark has one car in it and a second one enters
        Given the carpark has one car with number plate "HT12 GFS" in it
        When a car with number plate "RG22 TTY" enters the carpark
        Then a car with number plate "HT12 GFS" and a car with number plate "RG22 TTY" will occupy the carpark
    
    Scenario: The carpark is full and a car tries to enter
        Given a full carpark
        When a car with number plate "TO00 FUL" enters the carpark
        Then a car with number plate "TO00 FUL" will not occupy a space in the carpark