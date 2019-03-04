import re

def str2_in_str1(str2,str1):
	regex = re.compile(str2)
	result = regex.search(str1)
	return result.span() if result else None

print(str2_in_str1('abc','abc'))


"""
(0 + 0)

	参考答案的实现，用正则的效率比较低
"""