class Person():
    def __init__(self,name: str, age: int):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self.get_age()

    def SayHi(self):
        print(f"Hi, my name is {self._name} and I'm {self._age} years old")