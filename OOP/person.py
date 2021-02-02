class Person:
    def __init__(self, name, age, job):
        # print("Constructor")
        self.name = name
        self.age = age
        self.job = job
    def walk(self,km):
        return "walk " + str(km) + " Km"
    def __str__(self):
        """to String"""
        return  "Name: " + self.name+\
                "\nAge: " + str(self.age) +\
                "\nJob: " + self.job
    @staticmethod
    def do_sth():
        print("Static method")

