from math import pi


class Figure:
    def __init__(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y

    def draw(self, canvas):
        print("Draw figure with center ({} {}) on canvas".format(self.center_x, self.center_y))

    def area(self):
        print("Calculating Area")

    def __str__(self):
        return "Figure center: ({} {})".format(self.center_x, self.center_y)


class Circle(Figure):

    def __init__(self, center_x: int = 10, center_y: int = 5, radius: int = 20):

        super().__init__(center_x, center_y)
        self.radius = radius

    def draw(self, canvas):
        print("Draw OOOOOOOOOOOOOOOO")

    def area(self):
        print("The area of {1} is {0:.3f}".format(pi * self.radius**2, type(self)))


class Rectangle(Figure):
    def __init__(self, center_x: int = 10, center_y: int = 5, width: int = 20, height: int = 20):
        super().__init__(center_x, center_y)
        self.width = width
        self.height = height

    def draw(self, canvas):
        print("Draw [] [] [] [] [] []")

    def area(self):
        print("The area of the rectangle is {0:.3f}".format(self.width * self.height))


class Triangle(Figure):
    def __init__(self, center_x: int = 10, center_y: int = 5, base: int = 20, height: int = 10):
        super().__init__(center_x, center_y)
        self.base = base
        self.height = height

    def draw(self, canvas):
        print("Draw /\ /\ /\ /\ /\ /\ /\  ")

    def area(self):
        print("The area of the triangle is {0:.3f}".format(self.base * self.height))


figures = [
    Circle(0, 0, radius=10),
    Rectangle(0, 0, width=20.56, height=30.2),
    Triangle(0, 0, base=20, height=10)
]

for figure in figures:
    figure.area()


print(format(pi, '.10f'))