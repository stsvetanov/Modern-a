class Figure:
    def __init__(self, center_x, center_y, color='black'):
        self.center_x = center_x
        self.center_y = center_y
        self.color = color

    def print_info(self):
        print("Figure center: ({} {})".format(self.center_x, self.center_y))

    # def draw(self, canvas):
    #     print("Draw figure with center ({} {}) on canvas".format(self.center_y, self.center_y))

# Ако се опитаме да принтираме директно класа ще получим грешка
    def __str__(self):
        return "Figure center: ({} {})".format(self.center_x, self.center_y)


figure1 = Figure(5, 7)
print(figure1.center_x)
# figure1.print_info()
print(figure1)
