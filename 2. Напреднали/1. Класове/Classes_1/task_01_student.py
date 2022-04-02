class Student:
    def __init__(self, name, faculty_number, subjects=[]):
        self.name = name
        self.faculty_number = faculty_number
        self.subjects = subjects

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject_to_remove):
        try:
            self.subjects.remove(subject_to_remove)
        except:
            print(f'Subject {subject_to_remove} not found')
        else:
            print(f'Subject {subject_to_remove} removed')

    def print_subjects(self):
        print("Student {} has {}".format(self.name, self.subjects))

    def __str__(self):
        return f"name: {self.name}, faculty_number: {self.faculty_number}, subjects: {self.subjects}"


class School:
    def __init__(self, name):  # Constructor
        self.name = name
        self.students = []

    def add_student(self, faculty_number_to_add):
        self.students.append(faculty_number_to_add)

    def remove_student(self, faculty_number_to_remove):
        try:
            self.students.remove(faculty_number_to_remove)
        except:
            print(f'Faculty number {faculty_number_to_remove} not found')
        else:
            print(f'Faculty number {faculty_number_to_remove} removed')

    def __str__(self):
        return f'School name: {self.name}, Number of students: {len(self.students)}'


student1 = Student("Ivan", 234324234, ["Chemistry"])
print(student1.subjects)
student1.add_subject("Math")
student1.add_subject("Music")
print(student1.__str__())

student1.add_subject("Biology")
student1.print_subjects()

student2 = Student("Petar", 234329988)
student2.add_subject("Math")
student2.add_subject("Geography")
student2.print_subjects()

student1.remove_subject("Music")
print(student1.__str__())

my_school = School("Ivan Vazov")
my_school.add_student(student1.faculty_number)
my_school.add_student(student2)
print(my_school.__str__())
my_school.remove_student(234324234)
print(my_school.__str__())
