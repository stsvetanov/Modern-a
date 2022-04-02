class Animals:
    def __init__(self, age, sleep, eat):
        self.age = age

    def sleep(self):
        print("{} sleeps".format(self.name))

    def eat(self):
        print("{} eats".format(self.name))


class Pets(Animals):
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner


class Dog(Pets):
    def bark(self):
        print("{} barks : bau,bau".format(self.name))


class Cat(Pets):
    def meow(self):
        print("{} meow: Meoww".format(self.name))


dog1 = Dog("Sharo","Ivan")
dog1.bark()
dog1.sleep()
cat1 = Cat("Mali", "Elena")
cat1.eat()
cat1.meow()
