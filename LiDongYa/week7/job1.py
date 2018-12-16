# 1、请将 "1,2,3"，变成 ["1","2","3"]

s = "1,2,3"
# 方法一：内建函数
print(s.split(','))

# 方法二：函数实现
def str2list(s):
	lst = list()
	step = 0
	for i, value in enumerate(s):
		if value == ',':
			lst.append(s[step:i])
			step = i+1
	else:
		lst.append(s[step:])
	return lst

print(str2list(s))