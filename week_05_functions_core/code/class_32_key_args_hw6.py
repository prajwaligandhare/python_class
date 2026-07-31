# Ek function ko keyword arguments se call karke dikhao (order badal kar).

def intro(name, age):
    return print(f"My name is {name} and my age is {age}")

intro('akash', 30)  

intro(30, 'akash')
