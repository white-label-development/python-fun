def biggest_number(*args):
    print max(args)
    return max(args)
    
def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

print '------------------------'

def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
        
def rental_car_cost(days):
    total = days * 40
    discount = 0
    if days >= 7:
        discount = 50
    elif days >= 3:
        discount = 20
    
    return total-discount
    
def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money
    
    
print trip_cost('Los Angeles', 5, 600)