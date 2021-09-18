from Q3.Faculty import Faculty
from Q3.Professor import Professor


class Student(Faculty):
    def __init__(self, name: str, age: int, id: int):
        self._professor = Professor("",0,0)
        super(Student, self).__init__(name, age, id)

    def takingCourses(self):
        if (len(self._course)) > 0:
            print(f"I take these courses.{self._course}")
        else:
            print("I don’t take any course")

    def matchProfessor(self,prof):
        self._professor = prof
        self._professor.matchStudent(self.get_name())

    def professorName(self):
        if self._professor.get_name() != "":
            print(f"My professor is {self._professor.get_name()}")
        else:
            print("I don’t have an advisor professor yet.")