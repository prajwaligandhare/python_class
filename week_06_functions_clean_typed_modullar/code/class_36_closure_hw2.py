# 2. make_adder(n) closure banao jo n add kare; add5 = make_adder(5) test kare.

def make_adder(n):
    
    def add(x):
        return n + x

    return add

add5 = make_adder(5)

print(add5(5))

        




    

