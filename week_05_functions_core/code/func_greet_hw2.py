#2. Ek function greet(name, city) jo "Hi NAME from CITY" return kare (print nahi, return)

def greet(name, city):
    info = f" Hi my Name is {name} & I'm from {city} City"
    return info

greet_info = greet('payal', 'pune')    
print(greet_info)