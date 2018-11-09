#第一种
num = [1, 1]
i = 0
while num[i]+num[i+1] < 100:
    num.append(num[i]+num[i+1])
    i += 1
print(num)

#第二种
num1 = [1, 1]
for i in range(100):
    temp = num1[i]+num1[i+1]
    if temp < 100:
        num1.append(temp)
    else:
        break
print(num1)