class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the student_id here
        self.student_id = ""

    def create_id(self):
        self.student_id = self.name[0] + self.last_name + self.birth_year


student_name = input()
student_last = input()
student_year = input()
student = Student(student_name, student_last, student_year)
student.create_id()
print(student.student_id)
