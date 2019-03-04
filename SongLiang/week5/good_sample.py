import random

#方法1
def good_sample(**kwargs):
	#d = {'a':10, 'b':20, 'c':30, 'd':40}
	good = []
	num = []
	for k, v in kwargs.items():
		good.append(k)
		num.append(v)
	result = random.choices(good, num, k=1)
	return result

#方法2
def good_sample(**kwargs):
	specimen = []
	for k,v in kwargs.items():
		lst = []
		lst.append(k)
		lst *= v
		specimen += lst
	result = random.choice(specimen)
	return result

print(good_sample(a=10, b=20, c=30, d=40))

"""
(0 + 0)


"""