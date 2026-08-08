# 1. map + lambda se [1,2,3,4] ke har number ka cube banao.

num_1 = [1,2,3,4]

#map(function, items)

cube_numbers = list(map(lambda num: num ** 3, num_1))

print(cube_numbers)
