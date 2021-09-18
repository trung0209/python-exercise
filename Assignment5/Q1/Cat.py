from Q1.Feline import Feline

class Cat(Feline):

    def __init__(self,name, picture, food, hunger):
        super(Cat,self).__init__(picture,food,hunger)
        self.name = name

    def get_name(self):
        return self.name

    def makeNoise(self):
        print("Cat noise")

    def eat(self):
        print("Cat eat")