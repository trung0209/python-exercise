class Pokemon():
  def __init__(self,name,element,level):
      self.name = name
      self.level = level
      self.element = element
      self.maximum_health = level * 100
      self.current_health = level * 100
      self.is_knocked_out = False
# lose_health)
# and a method
# for regaining health.
# We also created a method that would
# officially “knock out” a Pokémon
# (when its health became 0)
# and another
# method to
# revive a knocked out Pokémon.
  def __repr__(self):
      return f"Pokemon: {self.name}, Level {self.level}" \
             f" Type: {self.element}, Health {self.maximum_health}"

  def lose_health(self,health):
      self.current_health -= health
      if self.current_health < 0:
        self.current_health= 0
        return self.check_isKnock_out()
      else:
        return f"{self.name} now has {self.current_health} health"

  def gain_health(self,heal):
      self.current_health += heal
      if self.current_health >= self.maximum_health:
        self.current_health = self.maximum_health
        return "pokemon is max health"
      else:
        return f"{self.name} now has {self.current_health} health"

  def check_isKnock_out(self):
      if self.current_health == 0:
          self.is_knocked_out = True
          return True
      else:
          self.is_knocked_out = False
          return False

  def revive(self,revive):
      if self.check_isKnock_out == True:
          if revive == True:
              self.current_health += 30
              self.is_knocked_out = False
              return f"{self.name} has been revived with 30 health"
      else:
        return f"your {self.name} is still alive cannot revive"

  def attack(self, other_pokemon):
      # Checks to make sure the pokemon isn't knocked out
      if self.is_knocked_out:
          print("{name} can't attack because it is knocked out!".format(name=self.name))
          return
      # If the pokemon attacking has a disadvantage, then it deals damage equal to half its level to the other pokemon
      if (self.element == "Fire" and other_pokemon.element == "Water") or (
              self.element == "Water" and other_pokemon.element == "Grass") or (
              self.element == "Grass" and other_pokemon.element == "Fire"):
          print("{my_name} attacked {other_name} for {damage} damage.".format(my_name=self.name,
                                                                              other_name=other_pokemon.name,
                                                                              damage=round(self.level * 0.5)))
          print("It's not very effective")
          other_pokemon.lose_health(round(self.level * 0.5))
      # If the pokemon attacking has neither advantage or disadvantage, then it deals damage equal to its level to the other pokemon
      if (self.element == other_pokemon.element):
          print("{my_name} attacked {other_name} for {damage} damage.".format(my_name=self.name,
                                                                              other_name=other_pokemon.name,
                                                                              damage=self.level))
          other_pokemon.lose_health(self.level)
      # If the pokemon attacking has advantage, then it deals damage equal to double its level to the other pokemon
      if (self.element == "Fire" and other_pokemon.element == "Grass") or (
              self.element == "Water" and other_pokemon.element == "Fire") or (
              self.element == "Grass" and other_pokemon.element
              == "Water"):
          print("{my_name} attacked {other_name} for {damage} damage.".format(my_name=self.name,
                                                                              other_name=other_pokemon.name,
                                                                              damage=self.level * 2))
          print("It's super effective")
          other_pokemon.lose_health(self.level * 2)

class Charmander(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Charmander", "Fire", level)

class Squirtle(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Squirtle", "Water", level)

class Bulbasaur(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Bulbasaur", "Grass", level)

class Trainer:
    # A trainer has a list of pokemon, a number of potions and a name. When the trainer gets created, the first pokemon in their list of pokemons is the active pokemon (number 0)
    def __init__(self, pokemon_list, num_potions, name):
        self.pokemons = pokemon_list
        self.potions = num_potions
        self.current_pokemon = 0
        self.name = name

    def __repr__(self):
        # Prints the name of the trainer, the pokemon they currently have, and the current active pokemon.
        print("The trainer {name} has the following pokemon".format(name = self.name))
        for pokemon in self.pokemons:
            print(pokemon)
        return "The current active pokemon is {name}".format(name = self.pokemons[self.current_pokemon].name)

    def switch_active_pokemon(self, new_active):
        # Switches the active pokemon to the number given as a parameter
        # First checks to see the number is valid (between 0 and the length of the list)
        if new_active < len(self.pokemons) and new_active >= 0:
            # You can't switch to a pokemon that is knocked out
            if self.pokemons[new_active].is_knocked_out:
                print("{name} is knocked out. You can't make it your active pokemon".format(name = self.pokemons[new_active].name))
            # You can't switch to your current pokemon
            elif new_active == self.current_pokemon:
                print("{name} is already your active pokemon".format(name = self.pokemons[new_active].name))
            # Switches the pokemon
            else:
                self.current_pokemon = new_active
                print("Go {name}, it's your turn!".format(name = self.pokemons[self.current_pokemon].name))

    def use_potion(self):
        # Uses a potion on the active pokemon, assuming you have at least one potion.
        if self.potions > 0:
            print("You used a potion on {name}.".format(name = self.pokemons[self.current_pokemon].name))
            # A potion restores 20 health
            self.pokemons[self.current_pokemon].gain_health(20)
            self.potions -= 1
        else:
            print("You don't have any more potions")

    def attack_other_trainer(self, other_trainer):
        # Your current pokemon attacks the other trainer's current pokemon
        my_pokemon = self.pokemons[self.current_pokemon]
        their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        my_pokemon.attack(their_pokemon)

# Six pokemon are made with different levels. (If no level is given, it is level 5)
a = Charmander(7)
b = Squirtle()
c = Squirtle(1)
d = Bulbasaur(10)
e = Charmander()
f = Squirtle(2)


#Two trainers are created. The first three pokemon are given to trainer 1, the second three are given to trainer 2.
trainer_one = Trainer([a,b,c], 3, "Alex")
trainer_two = Trainer([d,e,f], 5, "Sara")

print(trainer_one)
print(trainer_two)

# Testing attacking, giving potions, and switching pokemon.
trainer_one.attack_other_trainer(trainer_two)
trainer_two.attack_other_trainer(trainer_one)
trainer_two.use_potion()
trainer_one.attack_other_trainer(trainer_two)
trainer_two.switch_active_pokemon(0)
trainer_two.switch_active_pokemon(1)
print(trainer_one.pokemons[0])
print(trainer_one.pokemons[1])
print(trainer_one.pokemons[2])
print(trainer_two.pokemons[0])
print(trainer_two.pokemons[1])
print(trainer_two.pokemons[2])