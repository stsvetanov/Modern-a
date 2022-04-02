class molecule:
    def __init__(self,name='Generic'): # инициализиращ метод
        self.name = name
        self.atomlist = []
    def addatom(self, atom): # метод в класа
        self.atomlist.append(atom)
    def delatom(self,ind):
        self.atomlist.pop(ind)
    def get_mol(self):
        return (self.name,self.atomlist)
    # def __repr__(self): # метод променящ извеждането
    #     s = "Това е молекула с име " + self.name
    #     l=str(len(self.atomlist))
    #     s = s + "\nТя има "+ l+" атома:\n"
    #     for atom in self.atomlist:
    #         s = s + atom + '\n'
    #     return s

mol=molecule(name='ВОДА')
#mol=molecule()
mol.atomlist=['C','O','O']
# mol.addatom('H')
# mol.addatom('H')
# mol.addatom('O')
print(mol.name)
mol.name='Въглероден диоксид'
print(mol.name)
print(mol.get_mol())
# Изтриване на атом, вар.1: чрез директно използване на вградените методи, за типа на атрибута
mol.atomlist.pop(0)
# mol.atomlist връща списък, и от там нататък може да се прилагат всички методи, които са валидни за списъци

# Изтриване на том чрез създадения метод delatom(ind), вар.2:
mol.delatom(0)
# mol връща обект от тип molecule и може да използва всички методи на клас molecule

