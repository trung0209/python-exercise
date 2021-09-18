from Doctor import Doctor

class FamilyDoctor(Doctor):
    def __init__(self,name,hospital,houseVisits):
        self.houseVisits = houseVisits
        super().__init__(name,hospital)

    def giveAdvice(self):
        print("Give Advice method")