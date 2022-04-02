class molecule:
    def __init__(self,name='Generic'): # инициализиращ метод
        self.name = name
        self.atomlist = []
    def addatom(self, atom): # метод в класа
        self.atomlist.append(atom)
    def __repr__(self): # метод променящ извеждането
        s = "Това е молекула с име %s\n" %(self.name)
        s = s + "Тя има %d атома\n" %(len(self.atomlist))
        for atom in self.atomlist:
            s = s + str(atom) + '\n'
        return s


class atom(molecule): # този клас наследява класът molecule
    def __init__(self,atno,x,y,z): # инициализиращ метод
        self.atno = int(atno)
        self.position = (x,y,z)
    def symbol(self): # метод в класа
        mendeley={1:'H',2:'He',8:'O'}
        #Използваме речник, за който ключът е номера на елемента(атома) от периодичната таблица, а стойността е символното му означение
        return str(mendeley[self.atno])
    def __repr__(self): # метод променящ извеждането
        return '%d %s %10.4f %10.4f %10.4f' %(self.atno, self.symbol(), self.position[0],self.position[1],self.position[2])

# създаваме обект от тип molecule, като името на обекта е 'Вода'
# mol = molecule('Вода')

# Създаваме обект от тип atom, като му задаваме:
# --номера в периодичната таблица: atno
# --координатите на разположение: x,y,z
# at = atom(8,0.,0.,0.)

# за обекта mol добавяме нов атом, като използваме:
# --метода addatom от класа molecule
# --обекта at, създаден чрез класа atom
# mol.addatom(at)
# print(at)
# за обекта mol добавяме 2 нови атома, като използваме:
# --метода addatom от класа molecule
# --обекти, създадени чрез класа atom
# mol.addatom(atom(1,0.,0.,1.))

# Добавяне на нов атом като използваме метода append за списъци
# mol.atomlist.append(atom(1,0.,1.,0.))

# отпечатваме информацията за обекта mol
# print(mol)
#print(at)

#---------ИЗВЛИЧАНЕ НА ИНФОРМАЦИЯ---------
# print("Името на молекулата е: %s\n" %(mol.name))
# print("Списъкът от атоми в молекулата е:\n %s\n" %(mol.atomlist))
# print("Пълна информация за at:\n %s\n" %(at))
# print("Номер на атома в периодичната таблица: %d" %(at.atno)) # обект от клас X. атрибут към клас Х
# print("Позиции на атома в пространството:\n %s\n" %(str(at.position)))
# print("Символно означение на атома: %s" %(at.symbol())) # обект от клас X. метод към клас Х
# print("Имената на атомите в молекулата %s са: %s, %s, %s\n" %(mol.name, mol.atomlist[0].symbol(),mol.atomlist[1].symbol(),mol.atomlist[2].symbol()))
# обект от клас Х.атрибут от клас Х (този атрибут е списък с елементи от клас Y)[индекс]. метод от клас Y
# mol.atomlist е атрибута atomlist от класа molecule
# mol.atomlist[0] е от клас atom
# mol.atomlist[0].symbol()
# print("Извеждане на координатата x за първия атом, самата координата х също е първа от всичките три: %d\n" %(mol.atomlist[0].position[0]))
# обект от клас Х.атрибут от клас Х [индекс] => това реално е обект от клас Y
# обект от клас Y.атрибут от клас Y

# print("Извеждане на координатата z за втория атом, самата координата z също е трета от всичките три: %d\n" %(mol.atomlist[1].position[2]))

# да създам 3 обекта от клас molecule
ss=['Вода', 'Хелий','Кислород']
L=[molecule(s) for s in ss]

L[0].atomlist=[atom(1,0,0,0),atom(1,0,0,0),atom(8,0,0,0)]
L[1].atomlist=[atom(2,0,0,0),atom(2,0,0,0)]
L[2].atomlist=[atom(8,0,0,0),atom(8,0,0,0)]
print(L)