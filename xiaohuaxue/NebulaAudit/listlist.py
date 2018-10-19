
a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for c in a:
    print(c)

# for i in range(len(a)):
#     temp = []
#     for j in range(len(a[i])):
#         temp.append(a[j][i])
#     print(temp)

for i in range(len(a)):
    for j in range(i):
            a[j][i],a[i][j] = a[i][j],a[j][i]
print(a)


for i in list(enumerate(range(5))):
    print(i)

for i,val in list(enumerate(range(5))):
    print(i,val)