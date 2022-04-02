students = []

students.append(["Ivan Petrov", 654554, ["Math", "Biology", "Music"]])
students.append(["Stephan Dobrev", 657868, ["Math", "Biology", "Geography"]])
students.append(["Georgi Petrov", 654568, ["Math", "Biology", "Geography"]])


def add_subject(id, subject):
    for student in students:
        if id == student[1]:
            student[2].append(subject)


def remove_subject(id, subject):
    for student in students:
        if id == student[1]:
            # index_of_subject_to_remove = student[2].find(subject)
            student[2].remove(subject)


add_subject(657868, "Chemistry")
print(students)
remove_subject(657868, "Chemistry")
print(students)