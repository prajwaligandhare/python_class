# 2.Har error ke liye ek line likho: "Yeh error kab aata hai?"

a = 10 / 0
print("Yeh error kab aata hai? : ", a)
# ZeroDivisionError: division by zero

b = int('abc')
print("Yeh error kab aata hai? : ", b)
# ValueError: invalid literal for int() with base 10: 'abc'

c = [1,2,3][10]
print("Yeh error kab aata hai? : ", c)
# IndexError: list index out of range