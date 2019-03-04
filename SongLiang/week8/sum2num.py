def sum2num(lst,num):
	flag = False
	for n,i in enumerate(lst):
		for a in lst[n+1:]:
			if i + a == num:
				print('{} + {} = {}'.format(i,a,num))
				flag = True
	if not flag:
		print('No match')

sum2num([1,2,3,3,4,5,5],6)


"""
(0 + 0)

	还行！答案有更好的方法
"""