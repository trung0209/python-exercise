class Animal():
    def __init__(self,picture,food,hunger):
        self.picture = picture
        self.food = food
        self.hunger = hunger

    def get_pic(self):
        return self.picture

    def get_food(self):
        return self.food

    def get_hunger(self):
        return self.hunger

    def set_pic(self,picture):
        self.picture = picture

    def set_food(self,food):
        self.food = food

    def set_hunger(self,hunger):
        self.hunger = hunger

    def makeNoise(self):
        print("makeNoise")

    def sleep(self):
        print("Sleep")

    def roam(self):
        print("Roam in animal class")

    def eat(self):
        print(f"Animal eat")

    def __str__(self):
        return "Animal class"