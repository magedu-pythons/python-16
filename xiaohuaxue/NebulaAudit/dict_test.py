
# num_dict = dict(list(enumerate(input('请输入一串数字：'))))
# for v in num_dict.values():
#     count = 0
#     for k in num_dict:
#         if v == num_dict[k]:
#             count += 1
#     print(v+'重复'+str(count)+'次')

import random

nums = [random.randint(-1000, 1000) for i in range(100)]
nums_dict = dict(list(enumerate(sorted(nums), 1)))
lst_key = []  # 记录重复数的key
lst_count = {}  # 记录重复数的个数
for key, val in nums_dict.items():
    count = 1
    for k, v in nums_dict.items():
        if v == val and k != key:
            lst_key.append(k)
            count += 1
    lst_count[key] = count

for k in lst_key:
    nums_dict.pop(k)

for k, v in nums_dict.items():
    print(v)
    for key in lst_count:
        if key == k:
            print(lst_count[key])
            break