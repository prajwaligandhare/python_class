# 1. Ek function set_marks(m) jo 0-100 ke bahar value par ValueError raise kare.

def set_marks(m):
    if m < 0 or m > 100:
        raise ValueError("Marks must be between 0 and 100")
    return m    

print(set_marks(101))    

print(set_marks(85))