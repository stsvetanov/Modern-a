class Figure:
    def __init__(self, center_x, center_y, color='black'):
        self.center_x = center_x
        self.center_y = center_y
        self.color = color

    def __eq__(self, other):
        return (
            self.center_x == other.center_x
            and self.center_y == other.center_y
            and self.color == other.color
        )


...

f = Figure(10, 20, 'red')
f2 = Figure(1, 20, 'red')

...

print(f == f2)
print(f.__eq__(f2))
