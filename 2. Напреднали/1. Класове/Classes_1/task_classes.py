class Person:
    def __init__(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def eat(self):
        print(f"{self.name} eats.")

class Student(Person):

    def __init__(self,name, age, gender, id):
        super().__init__(name, age, gender)
        self.id = id
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def print_subjects(self):
        print(f"The student {self.name} has {self.subjects}")

    def __str__(self):
        return f"Name: {self.name}, ID:{self.id}, Subjects:{self.subjects} "


student1 = Student("Ivan",19,"Male", 140878)
student1.age = 19
student1.add_subject("Biology")
student1.print_subjects()

# student2 = Student("Nikola", 234567)
# student2.age = 21
# student2.gender = "Male"
# student2.add_subject("Informatics")
print(student1.__str__())