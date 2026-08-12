# 1. Shape parent; Triangle aur Square children, dono ka apna area().

class Shape:
    def __init__(self, name):
        self.name = name

class Triangle(Shape):
    def __init__(self, name, base, height):
     super().__init__(name)
     self.base = base
     self.height = height

    def area(self):
        return self.base * self.height / 2


class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def area(self):
        return self.side  * self.side

sh1 = Shape('Triangle')
tr = Triangle('Triangle', 5, 6)
print(tr.name, tr.base, tr.height)
print(tr.area())
sr = Square('Square', 10)
print(sr.name, sr.side)
print(sr.area())

