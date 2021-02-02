destinations=["Paris, France","Shanghai, China","Los Angeles, USA","São Paulo, Brazil","Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
attractions = [[] for x in range(5)]
import numpy as np
def get_destination_index(destination:str):
  destination_index= destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  traveler_destination = test_traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

def add_attraction(destination,attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
  except SyntaxError:
    return


def find_attractions(destination,interests:list):
  destination_index = get_destination_index(destination)
  attractions_in_city =  attractions[destination_index]
  attractions_with_interest = []

  for x in attractions_in_city:
    possible_attraction = x
    attraction_tags = x[1]
    for i in interests:
      if i in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

print(get_destination_index("Los Angeles, USA"))
print(get_destination_index("Paris, France" ))
test_destination_index = get_traveler_location(test_traveler)
add_attraction("Paris, France",
               ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

la_arts = find_attractions("Los Angeles, USA" ,['art'])
print(la_arts)