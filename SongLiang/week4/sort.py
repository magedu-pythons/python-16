#方法1：冒泡排序
import random
l = [random.randint(1,100) for _ in range(20)]
print(l)
for i in range(len(l)-1):
	flag = False
	for j in range(len(l)-i-1):
		if l[j] < l[j+1]:
			l[j],l[j+1] = l[j+1],l[j]
			flag = True
	if not flag:
		break
print(l[:3])

#方法2：选择排序
import random,math
l = [random.randint(1,100) for _ in range(20)]
print(l)
for i in range(math.ceil((len(l)-1)/2)):
	maxindex = i
	minindex = -i-1
	for j in range(i+1,len(l)-i):
		if l[j] > l[maxindex]:
			maxindex = j
		if l[-j-1] < l[minindex]:
			minindex = -j-1
	if maxindex == minindex:
		break
	if maxindex != i:
		l[i],l[maxindex] = l[maxindex],l[i]
		if minindex == i or i == len(l) + minindex:
			minindex = maxindex
	if (minindex != -i-1 or minindex != len(l)-i-1) and (l[minindex] != l[-i-1]):
		l[minindex],l[-i-1] = l[-i-1],l[minindex]
print(l[:3])

#方法3：插入排序
import random
l = [random.randint(1,100) for _ in range(20)]
print(l)
l1 = [0] + l
for i in range(2,len(l1)):
	l1[0] = l1[i]
	j = i - 1
	if l1[0] > l1[j]:
		while l1[0] > l1[j]:
			l1[j+1] = l1[j]
			j -= 1
		l1[j+1] = l1[0]
l1 = l1[1:]
print(l1[:3])


"""
(0 + 0)

	用函数封装
"""