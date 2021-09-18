from Doctor import Doctor
from Surgeon import Surgeon
from GeneralPractioners import GeneralPractioners
from FamilyDoctor import FamilyDoctor

test1 = Doctor("Docter 1","A")
test2 = GeneralPractioners("Practioners","B")
test3 = FamilyDoctor("Family doctor", "C", "House")
test4 = Surgeon("Surgeon doctor", "D")

print(type(test1))
print(test1.name)
print(test1.hospital)
test1.treatPatient()
print("#######################")
print(type(test2))
print(test2.name)
print(test2.hospital)
test2.treatPatient()
print("#######################")
print(type(test3))
print(test3.name)
print(test3.hospital)
test3.treatPatient()
test3.giveAdvice()
print("#######################")
print(type(test4))
print(test4.name)
print(test4.hospital)
test4.treatPatient()
test4.makeIncision()

