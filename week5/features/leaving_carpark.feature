Feature: Vehicles leaving the carpark

    Scenario: The carpark has one car in it and it leaves
        Given a carpark has one car with number plate "HT12 GFS" in it
        When a car with number plate "HT12 GFS" leaves the carpark
        Then the carpark will not contain a car with number plate "HT12 GFS" 