a = 1
b = 1
while a < 100:
	if b < 100:
		print(a,b,end=' ')
	else:
		print(a,end=' ')
	a += b
	b += a