from carpark import Carpark
from car import Car
from behave import *


# Scenario A carpark is partially full

@given(u'a carpark contains 5 cars and has a capacity of 15')
def step_impl(context):
    context.carpark = Carpark(15)
    for i in range(5):
        context.carpark.add_car(Car(f"car{i}"))


@when(u'we want to know how many spaces are taken and how many are free')
def step_impl(context):
    taken_free = context.carpark.spaces_taken_free()
    context.taken = taken_free[0]
    context.free = taken_free[1]


@then(u'we will be given the values 5 taken and 10 free')
def step_impl(context):
    assert context.taken == 5
    assert context.free == 10