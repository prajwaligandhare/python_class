#3. Ek Circle class with radius aur method area() jo area return kare.

class Circle:
     def __init__(self, radius):
         self.radius = radius


     def area(self):
         return 3.14 * self.radius ** 2

print(Circle(5).area())
         


         
         