from Q3.Faculty import Faculty


class Professor(Faculty):
    def __init__(self, name: str, age: int, id: int):
        self._students = list()
        super(Professor,self).__init__(name,age,int)

    def teachingCourses(self):
        if (len(self._course) > 0):
            print(f"I conduct these courses.{self._course}")
        else:
            print("I don’t teach any course.")

    def matchStudent(self, student):
        self._students.append(student)

    def studentsCount(self):
        if (len(self._students) > 0):
            print(f"I have {len(self._students)}")
        else:
            print("I have no students.")

    def studentsName(self):
        print("My students are ", end = "")
        for student in self._students:
            print(student.get_name(), end=",")