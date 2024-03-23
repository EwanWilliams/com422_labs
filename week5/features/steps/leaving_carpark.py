from carpark import Carpark
from car import Car
from behave import *


# Scenario The carpark has one car in it and it leaves

@given(u'a carpark has one car with number plate "HT12 GFS" in it')
def step_impl(context):
    context.carpark = Carpark(15)
    context.carpark.spaces[0] = Car("HT12 GFS")


@when(u'a car with number plate "HT12 GFS" leaves the carpark')
def step_impl(context):
    context.carpark.remove_car("HT12 GFS")


@then(u'the carpark will not contain a car with number plate "HT12 GFS"')
def step_impl(context):
    car_found = False
    for space in context.carpark.spaces:
        if space == None:
            continue
        elif space.reg == "HT12 GFS":
            car_found = True
    
    assert car_found == False
