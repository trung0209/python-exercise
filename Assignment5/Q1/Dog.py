from Q1.Canine import Canine

class Dog(Canine):

    def __init__(self,name, picture, food, hunger):
        super(Dog,self).__init__(picture,food,hunger)
        self.name = name

    def get_name(self):
        return self.name

    def makeNoise(self):
        print("Dog noise")

    def eat(self):
        print("Dog eat")


