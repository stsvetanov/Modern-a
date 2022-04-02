class student:
    def __init__(self,n,a):
        self.full_name =n
        self.age = a
    def get_age(self):
        return self.age
    def get_name(self):
        return self.full_name

class MI_student(student):
    def __init__(self,n,a,s, fn):
        student.__init__(self,n,a)
        self.stu =student.get_name(self)
        self.specialty=s
        self.fac_num=int(fn)
    def get_age(self):
        print("Възраст: ",str(self.age))
    def __repr__(self):
        return "Имена: %s, възраст: %d, Факултетен номер:%d специалност: %s" %(self.full_name, self.fac_num, self.age, self.specialty)

name="Деян Викторов"
ages=20
spec="МИ"
fnum=13888
st=student(name,ages)
print(st.get_age())
print(st)
st_2=MI_student(name,ages,spec, fnum)
st_2.get_age()
print(st_2.stu)
print(st_2)

