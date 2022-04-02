class Student:
    def __init__(self, name, faculty_number, subjects):
        self.name = name
        self.faculty_number = faculty_number
        self.subjects = subjects

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject_to_remove):
        try:
            self.subjects.remove(subject_to_remove)
        except:
            print(f'Subject {subject_to_remove} do not exits')
        else:
            print(f'Subject {subject_to_remove} removed')


student1 = Student("Ivan Petrov", 654554, ["Math", "Biology", "Music"])
student2 = Student("Stephan Dobrev", 657868, ["Math", "Biology", "Geography"])
student3 = Student("Georgi Petrov", 654568, ["Math", "Biology", "Geography"])

student2.add_subject("Chemistry")
print(student2.subjects)
student2.remove_subject("Chemistry2")
print(student2.subjects)