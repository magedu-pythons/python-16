test = (('a', 'b'), ('c', 'd'))

func = list(map(lambda x, y : {x:y}, test[0], test[1]))

print(func)