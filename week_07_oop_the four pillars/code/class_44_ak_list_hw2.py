# 1. Ek list mein alag shapes daalo aur loop se sabka area print karo.

class Shape:
    def __init__(self, name):
        self.name = name

class Triangle(Shape):
    def __init__(self,base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

class Square(Shape):
    def __init__(self,  side):
        self.side = side

    def area(self):
        return self.side ** 2

for a in [Square(5), Triangle(6,8)]:
    print(a.area())
                       
