line = int(input('输入*数量'))
if line % 2 == 0:
    line += 1
zline = line // 2
fline = -line // 2

for i in range(fline, zline + 1):
    print(abs(i)*' ' + '*' * (line - 2 * abs(i)))

