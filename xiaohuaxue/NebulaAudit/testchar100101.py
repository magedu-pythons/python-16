
m = input().strip().lstrip('0')
print('输入的是', len(m), '位数')

for c in m:
    print("第{}位为{}，它在{}中重复出现{}次".format(m.find(c)+1, c, m, m.count(c)))
print('end')
