def bus_ticket_price(age, student=False):
    STD_PRICE = 4

    price = STD_PRICE

    if age < 3 or age >= 65:
        price = 0
    elif age < 19 and student:
        price = price/2
    return price

def speeding_outcome(limit, speed_reported):
    outcome = [False, False]

    if speed_reported - limit > 10:
        outcome = [True, True]
    elif speed_reported > limit:
        outcome[0] = True
    return tuple(outcome)

def delivery_price(goods_value, distance):
    cost = 0

    if distance <= 10 and goods_value < 100:
        cost = 5
    elif distance > 10 and distance <= 20:
        cost = 10
    elif distance > 20 and distance <= 30:
        cost = 15
    elif distance > 30:
        cost = 15 + (0.5 * (distance - 30))

    return cost
