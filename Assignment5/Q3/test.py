from Q3.Person import Person
from Q3.Professor import Professor
from Q3.Student import Student

Jone = Person("Jone", 17)
Jone.SayHi()
Edison = Professor("Edison", 50, 612345)
Edison.SayHi()
Edison.addCourse("Software")
Edison.teachingCourses()
Edison.removeCourse("Software")
Edison.teachingCourses()

Jane = Student("Jane", 21, 19123456)

Jane.SayHi()
Jane.addCourse("Database")
Jane.addCourse("Sofware")
Jane.takingCourses()
Jane.removeCourse("Database")
Jane.takingCourses()
Jane.professorName()
Jane.matchProfessor(Edison)
Jane.professorName()
Edison.studentsCount()