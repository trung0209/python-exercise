from Q3.Person import Person


class Faculty(Person):
    def __init__(self, name: str, age: int, id: int):
        super(Faculty,self).__init__(name,age)
        self._id = id
        self._course = []

    def addCourse(self,course):
        self._course.append(course)

    def removeCourse(self,course):
        self._course.remove(course)