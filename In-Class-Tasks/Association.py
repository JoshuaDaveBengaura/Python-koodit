class Student:

    def __init__(self, name):
        self.name = name


class Teacher:

    def __init__(self):
        self.students = []

    def attendance_in(self, student):
        self.students.append(student)
        print(student.name + " present")
        return

    def attendance_out(self, student):
        self.students.remove(student)
        print(student.name + " absent/left")
        return

student1 = Student("Mikey")
student2 = Student("Gerard")
student3 = Student("Frank")
student4 = Student("Ray")
student5 = Student("Bob")
teacher = Teacher()

teacher.attendance_in(student1)
teacher.attendance_in(student2)
teacher.attendance_in(student3)
teacher.attendance_out(student3)
print(f"students in class: ", len(teacher.students))