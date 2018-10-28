# 给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0
lst = [1, 2, 3, 4, 5, 6, 5, 7, 8, 1, 3,]
x = int(input('Please input:'))		# 用户输入x元素
s = set(lst)  						# 换成集合，提高访问速度

if x in s:
    print('1')
else:
    print('0')