# multiply_all(*nums) jo saare numbers ka product return kare.

def multiply_all(*nums):
    values = 1

    for n in nums:
        values = values * n 
    return values

print(multiply_all(2, 3, 4))





