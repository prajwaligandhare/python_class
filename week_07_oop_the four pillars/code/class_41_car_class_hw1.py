# 1. Ek Car class banao with brand, speed, aur ek method drive() jo "BRAND is driving at SPEED" print kare.


class Car:
      def __init__(self, brand, speed):
          self.brand = brand
          self.speed = speed

      def drive(self):
          print(f" {self.brand} BRAND is driving at {self.speed} SPEED")


car1 = Car('MG', 120).drive()

#car1.drive()


          