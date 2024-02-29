def bus_ticket_price(age, student=False):
    STD_PRICE = 4

    price = STD_PRICE

    if age < 3 or age >= 65:
        price = 0
    elif age < 19 and student:
        price = price/2
    return price

def speeding_outcome(limit, speed_reported):
    outcome = (False, False)

    if speed_reported > limit:
        outcome[0] = True
    return outcome