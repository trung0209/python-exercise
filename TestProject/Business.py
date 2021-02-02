

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"{self.name} menu available from {self.start_time} to {self.end_time}"

    def calculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            if item in self.items:
                total += self.items[item]
        return total

class Franchise():
  def __init__(self,address,menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
      return "Our location is " + self.address
  def available_menus(self,time):
      available = []
      for i in self.menus:
        if time >= i.start_time and time <= i.end_time:
            available.append(i)
      return available

class Business():
    def __init__(self, name, franchises: list):
        self.name = name
        self.franchises = franchises
item = {'arepa pabellon': 7.00,
        'pernil arepa': 8.50,
        'guayanes arepa': 8.00,
        'jamon arepa': 7.50
        }
early_item = {'salumeria plate': 8.00,
              'salad and breadsticks (serves 2, no refills)': 14.00,
              'pizza with quattro formaggi': 9.00,
              'duck ragu': 17.50,
              'mushroom ravioli (vegan)': 13.50,
              'coffee': 1.50, 'espresso': 3.00}
brunch_items = {'pancakes': 7.50,
                'waffles': 9.00,
                'burger': 11.00,
                'home fries': 4.50,
                'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00,
                'mimosa': 10.50, 'orange juice': 3.50
                }

brunch = Menu("brunch",brunch_items,1100,1400)
early_bird = Menu("Early-bird",early_item,1300,1800)
menus = [brunch,early_bird]
arepas_menu = Menu("Take a’ Arepa",item,1000,2000)
new_installment = Franchise("12 East Mulberry Street",menus)
flagship_store = Franchise("1232 West End Road",menus)
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

store = [new_installment,flagship_store,arepas_place]

new_business = Business("Take a' Arepa",store)
print(new_business.franchises)
print(new_business.franchises[2].available_menus(1200))
print(new_business.franchises[2].menus)

# first = Business("Basta Fazoolin' with my Heart",store)