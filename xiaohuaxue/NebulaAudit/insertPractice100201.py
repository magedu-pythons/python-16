
#直接插入排序
num = [1, 56, 8, 69, 47, 32, 958, 42, 563, 245, 14, 5895, 5, 8456]

num.insert(0, 0)

for i in range(2, len(num)):
    if int(num[i]) >= int(num[i-1]):
        continue
    else:
        num[0] = num[i]
        num[i] = num[i-1]
        for j in range(i-2):
            if int(num[0]) >= int(num[i-2-j]):
                num[i-1-j] = num[0]
                break
            else:
                num[i-1-j] = num[i-2-j]
num.pop(0)
print(num)

#[1, 5, 8, 14, 32, 42, 47, 56, 69, 245, 563, 958, 5895, 8456]
#[1, 5, 8, 14, 32, 42, 47, 56, 69, 245, 563, 958, 5895, 8456]