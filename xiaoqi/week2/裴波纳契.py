#方法一
a1 = 0
a2 = 1
while True:
    a3 = a1 + a2
    if a3 > 100:
        break
    a1 = a2
    a2 = a3
    print(a3)
#方法二
number = [1, 1]
for i in range(100):
    val = number[i] + number[i + 1]
    if val >= 100:
        break
    else:
        number.append(val)
print(number)
