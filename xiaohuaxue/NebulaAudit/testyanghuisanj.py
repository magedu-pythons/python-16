
triangle = [[1], [1, 1]]
n = 20
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
# m = 9
# k = 5
# n = m - 1
# r = k - 1
# d = n - r
# targets = [] #r,n-r,n
# factorial = 1
# for i in range(1,n+1):
#     factorial *= i
#     if i == r:
#         targets.append(factorial)
#     if i == d:
#         targets.append(factorial)
#     if i == n:
#         targets.append(factorial)
#
# print(targets[2] // (targets[0]*targets[1]))
