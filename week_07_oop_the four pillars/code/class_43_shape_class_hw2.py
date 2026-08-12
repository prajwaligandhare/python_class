# 2.Shape parent (with name); Square aur Rectangle children with super().

class Shape:
    def __init__(self, name):
        self.name = name

class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width


    def area(self):
        return self.length * self.width

shape1 = Shape('shape')
print(shape1.name)

square1 = Square('square', 5)
print(square1.area())

rectangle1 = Rectangle('rectangle', 10, 20)
print(rectangle1.area())




           


        