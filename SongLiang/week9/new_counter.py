def new_counter(num):
	def new_number():
		nonlocal num
		num += 1
		return num
	return new_number

c1 = new_counter(10)
c2 = new_counter(20)
print(c1(),c2(),c1(),c2())