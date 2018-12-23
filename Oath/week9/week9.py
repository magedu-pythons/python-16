# 18 请实现函数new_counter,使得调用结果：
# 	c1 = new_counter(10)
# 	c2 = new_counter(20)
# 	print(c1(), c2(), c1(), c2()) -> 11, 21, 12, 22
#
def new_counter(num:int=0) -> int:
	def inc():
		nonlocal num
		num += 1
		# target = num + 1
		# return target
		return num
	return inc
c1 = new_counter(10)
c2 = new_counter(20)
print(c1(), c2(), c1(), c2())
#
# 19、实现一个函数，输入字符串，判断该字符串是否不含有重复字符
def str_repeat(m_str:str=''):
	if not m_str or not isinstance(m_str, str):
		m_str = input('please input a string:')
	for i ,val in enumerate(m_str):
		if m_str[i+1:].find(val) != -1:
			return '{} have repeat char'.format(m_str)
	return '{} have not repeat char'.format(m_str)
print(str_repeat('abcdef'))
#
def str_repeat(m_str:str=''):
	if not m_str or not isinstance(m_str, str):
		m_str = input('please input a string:')
	return 'repeat' if len(m_str) > len(set(m_str)) else 'not repeat'
print(str_repeat('abcdea'))
#
def str_repeat(m_str:str=''):
	if not m_str or not isinstance(m_str, str):
		m_str = input('please input a string:')
	for i, val in enumerate(m_str):
		if val in m_str[i+1:]:
			return 'repeat'
	return 'not repeat'
print(str_repeat('abcdefa'))
#
str_repeat = lambda m_str: 'repeat' if len(m_str) > len(set(m_str)) else 'not repeat'
print(str_repeat('abcdefa'))