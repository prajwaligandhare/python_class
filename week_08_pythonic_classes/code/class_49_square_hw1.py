# 1. Square class mein area property banao.

class Square:
    def __init__(self, side):
        self.side = side
    @property
    def area(self):
        return self.side * self.side
print(Square(5).area)           