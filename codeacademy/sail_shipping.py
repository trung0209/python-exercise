Premium = 125.00

def ground_shipping(weight):
  price_per_pound = 0
  if (weight <= 2):
    price_per_pound = 1.50
  elif (weight > 2) and (weight <= 6):
    price_per_pound = 3.00
  elif (weight > 6) and (weight <= 10):
    price_per_pound = 4.00
  elif (weight > 10) :
    price_per_pound = 4.75
  total = price_per_pound * weight + 20.00
  return total

def drone_shipping(weight):
  price_per_pound = 0
  if (weight <= 2):
    price_per_pound = 4.50
  elif (weight > 2) and (weight <= 6):
    price_per_pound = 9.00
  elif (weight > 6) and (weight <= 10):
    price_per_pound = 12.00
  elif (weight > 10) :
    price_per_pound = 14.25
  total = price_per_pound * weight
  return total

def cheapest_method(weight):
  method = ""
  total = 0
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  if (ground < drone) and (ground < Premium):
    method = "Ground Shipping"
    total = ground
  elif (ground > drone) and (drone < Premium):
    method = "Drone Shipping"
    total = drone
  elif (ground > Premium) and (drone > Premium):
    method = "Premium Ground Shipping"
    total = Premium
  else:
    method = "All same"
    total = Premium

  print(f"The shipping method that is cheapest is {method},the total cost {total} to ship a package of {weight}")