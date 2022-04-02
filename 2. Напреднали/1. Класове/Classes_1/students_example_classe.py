class Student:
    name = None
    faculty_number = None
    subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject):
        self.subjects.remove(subject)


student1 = Student()
student2 = Student()

student2.add_subject("Chemistry")
print(student2.subjects)

student2.remove_subject("Chemistry")
print(student2.subjects)

student1.name = "Dimitar"
print(student1.name)
print(student2.name)
