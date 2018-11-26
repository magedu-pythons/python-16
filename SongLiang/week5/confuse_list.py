import random

#方法1
alist = [1,2,3,4,5]
random.shuffle(alist)
print(alist)

#方法2
alist = [1,2,3,4,5]
l = random.sample(alist,len(alist))
print(l)

#方法3
def confuse_list(src, dst=[]):
	if len(src) > 0:
		a = random.choice(src)
		src.remove(a)
		dst.append(a)
		return confuse_list(src)
	else:
		return dst

alist = [1,2,3,4,5]
print(confuse_list(alist))

"""
(0 + 0)

	函数形式参数不要用list
"""