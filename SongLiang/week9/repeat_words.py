#方法1
def repeat_words(s):
	for i in s:
		if s.count(i) > 1:
			print('It has repeat word')
			return
	else:
		print('There are no repeat word')

repeat_words('aabc')

#方法2
def repeat_words(s):
	lst = []
	for i in s:
		if i in lst:
			print('It has repeat word')
			return
		else:
			lst.append(i)
	else:
		print('There are no repeat word')

repeat_words('abc')

#方法3
def repeat_words(s):
	for i in range(1,len(s)):
		if s[i] in s[0:i]:
			print('It has repeat word')
			return
	else:
		print('There are no repeat word')

repeat_words('acc')