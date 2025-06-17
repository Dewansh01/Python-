import geopy.distance

def get_distance(location_1 , location_2):
  distance = geopy.distance.distance(location_1 , location_2).km

  return distance

def get_price_per_km(hour):
  if (hour > 8) & (hour < 11):
    price = 20
  elif (hour > 18) & (hour < 21):
    price = 15

  else:
    price = 10

  return price


def get_total_price(pickup_location , drop_location , booking_hour):
  total_distance = get_distance(pickup_location , drop_location)
  actual_price_per_km = get_price_per_km(booking_hour)

  final_price = round(total_distance * actual_price_per_km , 2)

  return final_price


pick_up_location = (24, 70)
drop_location = (24.1, 70.1)
booking_hour = 19


get_total_price(pick_up_location, drop_location, booking_hour)

output :  225.56
'''it calculates the distance from pune to nagpur and tell's the price as per given credencitial'''

















