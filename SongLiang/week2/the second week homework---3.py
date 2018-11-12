import random

lst = []
while len(lst) < 200:
	s = ''
	for d in range(6):
		s += str(random.randint(0,9))
	if s in lst:
		continue
	else:
		lst.append(s)
print(lst)

"""
(0 + 0)

	逻辑上没问题，优惠码需要加上字符
"""