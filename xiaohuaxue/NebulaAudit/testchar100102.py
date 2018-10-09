
num = input('请输入数值').strip().lstrip('0')

count = [0] * 10

for i in range(10):
    count[i] = num.count(str(i))


for j in range(10):
    if count[j]:
        print(j, count[j])
lst = list(num)
lst.reverse()
print(lst)

