#{1,2,3,4} ke har number ka cube ek dict comprehension se banao {num: cube}.

num = {1, 2, 3, 4}

comprhn_cube = {n : n ** 3 for n in num}

print(comprhn_cube)
