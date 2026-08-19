# 3. Ek Counter class banao jisme class attribute total ho jo har object par badhe.

class Counter:
    total = 0
    def __init__(self):
        Counter.total += 1

Counter(); Counter(); Counter();
print(Counter.total)        

