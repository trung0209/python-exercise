from Q1.Cat import Cat
from Q1.Lion import Lion
from Q1.Dog import Dog

lion = Lion("Lion pic","meat",5)
print(f"Pic: {lion.get_pic()}")
print(f"Food: {lion.get_food()}")
print(f"Hunger: {lion.get_hunger()}")

lion.eat()
lion.set_hunger(1)
print(f"Hunger: {lion.get_hunger()}")

lion.makeNoise()
lion.roam()
lion.sleep()

dog = Dog("Mikey","Dog pic", "dog food", 2)

print(dog.get_name())
print(dog.get_pic())
print(dog.get_food())
print(dog.get_hunger())

dog.makeNoise()
dog.eat()
dog.sleep()
dog.roam()

cat = Cat("Meow","cat pic", "cat food", 1)

print(cat.get_name())
print(cat.get_pic())
print(cat.get_food())
print(cat.get_hunger())

cat.makeNoise()
cat.eat()
cat.sleep()
cat.roam()