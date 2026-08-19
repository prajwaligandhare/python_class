# 2. Temperature class mein staticmethod c_to_f(c) add karo.
class Temperature:
    @staticmethod
    def c_to_f(c):
        return (c * 9 / 5) + 32
print(Temperature.c_to_f(37))        