# 2. Ek Temperature class banao with _celsius; ek method set_celsius jo -273 se kam value reject kare.
# 2
class Temperature:
    def __init__(self):
        self._celsius = 0
    def set_celsius(self, value):
        if value < -273:
            print("Below absolute zero — invalid!")
            return
        self._celsius = value
    def get_celsius(self):
        return self._celsius
t = Temperature()
t.set_celsius(-300)     # Below absolute zero — invalid!
t.set_celsius(25)
print(t.get_celsius())                  