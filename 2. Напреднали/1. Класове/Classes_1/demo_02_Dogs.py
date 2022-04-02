class Dog:
    def __init__(self, name="sharo", gender="male", age=5):
        self.name = name
        self.age = age
        self.gender = gender


    def bark(self):
        print(f"{self.name}: Bau bau")

    def eat(self):
        print("The {} {} eats".format(self.__class__.__name__, self.name))

    def sleep(self):
        print("{}: sleeps".format(self.name))


dog_1 = Dog("Sharo", age=2)

dog_2 = Dog()
dog_2.name = "Buki"
print(dog_2.name)

dog_2.name = "Buki"

print(dog_1.age)
print(dog_1.name)
print(dog_2.name)


dog_1.bark()
dog_2.bark()
dog_2.eat()


