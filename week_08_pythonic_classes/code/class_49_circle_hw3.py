# 3. Circle mein diameter property banao (2 * radius).

class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius
circle = Circle(5)
print(circle.diameter)
