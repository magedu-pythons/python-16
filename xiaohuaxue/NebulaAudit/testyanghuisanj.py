import math
triangle = [[1], [1, 1]]
n = 11
for i in range(1, n-1):
    top = [1]
    for j in range(i):
        mid = triangle[i][j] + triangle[i][j+1]
        top.append(mid)
    top.append(1)
    triangle.append(top)
for c in range(len(triangle)):
    a = ' '
    y = str(triangle[c])
    yy_max = str(triangle[len(triangle)-1])
    yy_max_count = len(yy_max)
    count = int((yy_max_count-len(y))/2)
    print('{}{}'.format(a*count, y))

