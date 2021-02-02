from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# Build your program below:
landmark_string = ""
for letter, landmark in landmark_choices.items():
  landmark_string += "{0} - {1}\n".format(letter, landmark)


def greet():
  print("""Hi there and welcome to SkyRoute!"
"We'll help you find the shortest route between the following Vancouver landmarks:\n""" + landmark_string)
  skyroute()


def skyroute():
  greet()
  new_route()
  goodbye()


def set_start_and_end(start_point, end_point):
  if start_point != None:
      change_point = input(
        "What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
      if change_point == "b":
        start_point = get_start()
        end_point = get_end()
      elif change_point == "o":
        start_point = get_start()
      elif change_point == "o":
        end_point = get_end()
      else:
        print("Oops, that isn't 'o', 'd', or 'b'...")
        set_start_and_end(start_point, end_point)
  else:
    start_point = get_start()
    end_point = get_end()
  return start_point, end_point


def get_start():
  start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
  if start_point_letter in landmark_choices.keys():
    start_point = landmark_choices[start_point_letter]
  return start_point


def get_end():
  end_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")
  if end_point_letter in landmark_choices.keys():
    end_point = landmark_choices[end_point_letter]
  return end_point


def new_route(start_point, end_point):
  start_point, end_point = set_start_and_end(start_point, end_point)
  shortest_route = get_route(start_point, end_point)
  shortest_route_string = "\n".join(shortest_route)
  print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
  again = input("Would you like to see another route? Enter y/n: ")
  if again == "yes":
    show_landmarks()
    new_route(start_point, end_point)


def show_ladnmarks():
  see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")
  if see_landmarks == "y":
    print(landmark_string)


def get_route(start_point, end_point):
  start_stations = vc_landmark[start_point]
  end_stations = vc_landmark[end_point]
  routes = []
  for start_station in start_stations:
    for end_station in end_stations:
      route = bfs(vc_metro, start_station, end_station)
      if route is not None:
        routes.append(route)
  shortest_route = min(routes, key=len)


def goodbye():
  print("Thanks for using SkyRoute")




