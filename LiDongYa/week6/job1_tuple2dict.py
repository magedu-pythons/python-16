# 现有两元祖 (('a'),('b')),(('c'),('d')) ,请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'b':'d'}]

func = lambda x, y:[dict((item,)) for item in zip(x, y)]

print(func((('a'),('b')), (('c'),('d'))))	# 打印结果[{'a': 'c'}, {'b': 'd'}]
