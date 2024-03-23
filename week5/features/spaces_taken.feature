Feature: Return number of taken spaces and number of free spaces

    Scenario: A carpark is partially full
        Given a carpark contains 5 cars and has a capacity of 15
        When we want to know how many spaces are taken and how many are free
        Then we will be given the values 5 taken and 10 free