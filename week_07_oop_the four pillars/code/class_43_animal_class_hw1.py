# 1. Animal parent banao; Cat aur Cow children banao, har ek apni awaaz wala method.

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eat food")

class Cat(Animal):
        def speek(self):
            print(f"{self.name} says Meow Meow")

class Cow(Animal):
        def speek(self):
            print(f"{self.name} syas Hmbhaaaaa")


animal1 = Animal("CAT")
animal1.eat()

cat1 = Cat("Kitty")
cat1.speek()
cat1.eat()

cow1 = Cow("Yamuna")
cow1.speek()
cow1.eat()



