class Fillable:

    def __init__(self):
        print("Fillable __init__")

    def fill(self):
        print("Fill")


class Figure:
    def __init__(self, center_x, center_y, color='black'):
        self.center_x = center_x
        self.center_y = center_y
        self.color = color

    # def print_info(self):
    #     print("Figure center: ({} {})".format(self.center_x, self.center_y))

    def draw(self, canvas):
        print("Draw figure with center ({} {}) on canvas".format(self.center_x, self.center_y))

# Ако се опитаме да принтираме директно класа ще получим грешка
    def __str__(self):
        return "Figure center: ({} {})".format(self.center_x, self.center_y)


class Circle(Figure):

    def __init__(self, center_x: int = 10, center_y: int = 5, radius: int = 20):

        super().__init__(center_x, center_y)
        self.radius = radius

    # override
    def draw(self, canvas):
        print("Draw OOOOOOOOOOOOOOOO")

    def _secret_action(self):
        print("Secret")


class Rectangle(Figure):
    def __init__(self, center_x: int = 10, center_y: int = 5, width: int = 20, height: int = 20):
        super().__init__(center_x, center_y)
        self.width = width
        self.height = height

    # override
    def draw(self, canvas):
        print("Draw [] [] [] [] [] []")


class Triangle(Figure, Fillable):
    def __init__(self, center_x: int = 10, center_y: int = 5, side: int = 20):
        super().__init__(center_x, center_y)
        self.side = side

    # override
    def draw(self, canvas):
        print("Draw /\ /\ /\ /\ /\ /\ /\  ")

    def call_super(self):
        super().draw(None)


figures = [
    Circle(0, 0, radius=10),
    Rectangle(0, 0, width=20, height=30),
    Triangle(0, 0, side=20)
]

for figure in figures:
    figure.draw(None)

triangle1 = figures[2]
triangle1.call_super()


triangle1.fill()





