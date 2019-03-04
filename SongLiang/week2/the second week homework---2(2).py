l = [1,1]
while l[-1] < 100:
	l.append(l[-1]+l[-2])
print(l[:-1])