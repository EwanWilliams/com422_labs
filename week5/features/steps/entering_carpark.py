from carpark import Carpark
from car import Car
from behave import *


# Scenario The carpark is empty and a car enters

@given(u'an empty carpark')
def step_impl(context):
    context.carpark = Carpark(15)


@when(u'a car with number plate "HT12 GFS" enters the carpark')
def step_impl(context):
    context.carpark.add_car(Car("HT12 GFS"))


@then(u'a car with number plate "HT12 GFS" occupies a space in the carpark')
def step_impl(context):
    assert context.carpark.spaces[0].reg == "HT12 GFS"


# Scenario The carpark has one car in it and a second one enters

@given(u'the carpark has one car with number plate "HT12 GFS" in it')
def step_impl(context):
    context.carpark = Carpark(15)
    context.carpark.spaces[0] = Car("HT12 GFS")


@when(u'a car with number plate "RG22 TTY" enters the carpark')
def step_impl(context):
    context.carpark.add_car(Car("RG22 TTY"))


@then(u'a car with number plate "HT12 GFS" and a car with number plate "RG22 TTY" will occupy the carpark')
def step_impl(context):
    assert context.carpark.spaces[0].reg == "HT12 GFS" and context.carpark.spaces[1].reg == "RG22 TTY"


# Scenario The carpark is full and a car tries to enter
@given(u'a full carpark')
def step_impl(context):
    context.carpark = Carpark(15)
    for i in range(15):
        context.carpark.add_car(Car(f"car{i}"))


@when(u'a car with number plate "TO00 FUL" enters the carpark')
def step_impl(context):
    context.carpark.add_car(Car("TO00 FUL"))


@then(u'a car with number plate "TO00 FUL" will not occupy a space in the carpark')
def step_impl(context):
    car_found = False
    for space in context.carpark.spaces:
        if space.reg == "TO00 FUL":
            car_found = True
    
    assert car_found == False
    assert len(context.carpark.spaces) == context.carpark.size
    