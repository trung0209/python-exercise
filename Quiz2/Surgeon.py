from Doctor import Doctor

class Surgeon(Doctor):
    def __init__(self, name, hospital):
        super().__init__(name,hospital)

    def treatPatient(self):
        print("Surgeon Treat patient method")

    def makeIncision(self):
        print("makeIncision method")
