class Admissions:
    def __init__(self):
        self.max_student_department = None
        self.student_gpa_list = []
        self.biotech_list = []
        self.chemistry_list = []
        self.engineering_list = []
        self.mathematics_list = []
        self.physics_list = []
        self.department_dict = {"Biotech": self.biotech_list,
                                "Chemistry": self.chemistry_list,
                                "Engineering": self.engineering_list,
                                "Mathematics": self.mathematics_list,
                                "Physics": self.physics_list}
        self.main()

    def get_max_students(self):
        self.max_student_department = int(input())

    def read_file(self):
        with open('applicants.txt', 'r') as file:
            for line in file:
                first, last, phys, chem, math, cs, final, planA, planB, planC = line.split()
                self.student_gpa_list.append([first + " " + last,
                                              round((float(phys) + float(math)) / 2, 1) if round((float(phys) + float(math)) / 2, 1) > float(final) else float(final),
                                              round(float(chem), 1) if round(float(chem), 1) > float(final) else float(final),
                                              round(float(math), 1) if round(float(math), 1) > float(final) else float(final),
                                              round((float(cs) + float(math)) / 2, 1) if round((float(cs) + float(math)) / 2, 1) > float(final) else float(final),
                                              round((float(chem) + float(phys)) / 2, 1) if round((float(chem) + float(phys)) / 2, 1) > float(final) else float(final),
                                              planA, planB, planC])

    def sort_students(self, plan):
        def sort_students_into_departments(sort_by_index1, sort_by_index2, department, index):
            self.student_gpa_list.sort(key=lambda x: (-x[sort_by_index1], x[sort_by_index2]))
            self.student_gpa_list.reverse()
            for i in range(len(self.student_gpa_list) - 1, -1, -1):
                if len(self.department_dict.get(department)) < self.max_student_department \
                        and self.student_gpa_list[i][index] == department:
                    name = self.student_gpa_list[i][sort_by_index2]
                    test = self.student_gpa_list[i][sort_by_index1]
                    self.department_dict.get(department).append([name, test])
                    del self.student_gpa_list[i]

        if plan == "A":
            index = 6
        elif plan == "B":
            index = 7
        elif plan == "C":
            index = 8

        sort_students_into_departments(2, 0, "Chemistry", index)
        sort_students_into_departments(5, 0, "Biotech", index)
        sort_students_into_departments(4, 0, "Engineering", index)
        sort_students_into_departments(3, 0, "Mathematics", index)
        sort_students_into_departments(1, 0, "Physics", index)

    def print_list(self):
        for department in self.department_dict.keys():
            print(department)
            if len(self.department_dict.get(department)) >= self.max_student_department:
                length_of_iter = self.max_student_department
            else:
                length_of_iter = len(self.department_dict.get(department))
            for i in range(length_of_iter):
                name = self.department_dict.get(department)[i][0]
                gpa = self.department_dict.get(department)[i][1]
                print(name, gpa)
            print()

    def save_list(self):
        for department in self.department_dict.keys():
            with open(f'{department}.txt', 'w') as file:
                if len(self.department_dict.get(department)) >= self.max_student_department:
                    length_of_iter = self.max_student_department
                else:
                    length_of_iter = len(self.department_dict.get(department))
                for i in range(length_of_iter):
                    name = self.department_dict.get(department)[i][0]
                    gpa = self.department_dict.get(department)[i][1]
                    file.write(name + " " + str(gpa) + '\n')

    def main(self):
        self.get_max_students()
        self.read_file()

        self.sort_students("A")
        self.sort_students("B")
        self.sort_students("C")

        self.biotech_list.sort(key=lambda x: (-x[1], x[0]))
        self.chemistry_list.sort(key=lambda x: (-x[1], x[0]))
        self.engineering_list.sort(key=lambda x: (-x[1], x[0]))
        self.mathematics_list.sort(key=lambda x: (-x[1], x[0]))
        self.physics_list.sort(key=lambda x: (-x[1], x[0]))

        self.print_list()
        self.save_list()


Admissions()
