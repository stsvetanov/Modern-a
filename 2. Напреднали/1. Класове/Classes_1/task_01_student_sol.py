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
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.students = []

    def add_student(self, id):
        self.students.append(id)

    def remove_student(self, faculty_number_to_remove):
        try:
            self.students.remove(next(filter(lambda x: x.faculty_number == faculty_number_to_remove, self.students)))
        except:
            print(f'Faculty number {faculty_number_to_remove} not found')
        else:
            print(f'Faculty number {faculty_number_to_remove} removed')

        # removed = False
        # for index, student in enumerate(self.students):
        #     faculty_number = student.faculty_number
        #
        #     if faculty_number == faculty_number_to_remove:
        #         removed = self.students.pop(index)
        #         print(f'Student: {faculty_number_to_remove} removed.')
        #         break
        # if not removed:
        #     print(f'Student: {faculty_number_to_remove} not found.')

    def create_student(self, name, id, subjects=[]):
        self.students.append(Student(name, id, subjects))

    def print_students(self):
        for student in self.students:
            print(student.__str__())


my_school = School("Ivan Vazov", "24")
my_school.create_student("Ivan", 234324234, ["Chemistry"])
my_school.create_student("Petar", 234329988)
my_school.print_students()
my_school.remove_student(23432998854)
my_school.print_students()


