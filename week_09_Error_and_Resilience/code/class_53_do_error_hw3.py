# 3. Do errors (ZeroDivisionError, ValueError) ko ek hi handler se pakdo.

try:
    a = int("abc")
    b = 10 / 0
except (ZeroDivisionError, ValueError) as e:
    print(f"Math/Value error: {e}") 
       