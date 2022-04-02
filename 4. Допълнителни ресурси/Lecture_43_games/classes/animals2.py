class Animal:
    def __init__(self, age):
        self.age = age

    def sleep(self):
        print(f"The {self.__class__.__name__} {self.name} sleeps")

    def eat(self):
        print("{} eats".format(self.name))


class Pet(Animal):
    def __init__(self, name, owner, age):
        self.name = name
        self.owner = owner
        super().__init__(age)


class Dog(Pet):
    # def __init__(self, name, owner):
    #     super().name = name
    #     super().owner = owner

    def bark(self):
        print(f"The {self.__class__.__name__} {self.name}: bau bau")


class Cat(Pet):
    # def __init__(self, name, owner):
    #     self.name = name
    #     self.owner = owner
    def miau(self):
        print("{}: miau".format(self.name))


dog1 = Dog("Sharo", "John Smith", 3)
dog1.bark()
dog1.age = 7
dog1.sleep()

cat1 = Cat("Kuma Lisa", "Ivan Ivanov", 2)
cat1.miau()