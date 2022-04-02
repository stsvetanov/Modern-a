class Figure:
    def __init__(self, center_x, center_y, color='black'):
        self.center_x = center_x
        self.center_y = center_y
        self.color = color

    # def print_info(self):
    #     print("Figure center: ({} {})".format(self.center_x, self.center_y))

    def draw(self, canvas):
        print("Draw {} with center ({} {}) on canvas".format(self.__class__.__name__, self.center_x, self.center_y))

# Ако се опитаме да принтираме директно класа ще получим грешка
    def __str__(self):
        return "Figure {} with center: ({} {})".format(self.__class__.__name__, self.center_x, self.center_y)


class Circle(Figure):

    def __init__(self, center_x: int = 10, center_y: int = 5, radius: int = 20):
        # super().center_x = center_x
        # super().center_y = center_y
        super().__init__(center_x, center_y)
        self.radius = radius

    # override
    # def draw(self, canvas):
    #     print("Draw OOOOOOOOOOOOOOOO")

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


class Triangle(Figure):
    def __init__(self, center_x: int = 10, center_y: int = 5, side: int = 20):
        super().__init__(center_x, center_y)
        self.side = side

    # override
    def draw(self, canvas):
        print("Draw /\/\/\/\/\/\/\\")


circle = Circle(0, 0, 20)
circle.draw(None)

figure1 = Figure(5, 7)
# figure1.print_info()
print(figure1)

circle1 = Circle(center_x=20, center_y=35, radius=20)
circle1.draw(None)
print(circle1)

triangle1 = Triangle(center_x=20, center_y=35, side=20)
triangle1.draw(None)



