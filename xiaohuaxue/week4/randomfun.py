
#任意生成20个数字，选取前3个大数
import random

lst = [random.randint(1,1000) for i in range(20)]
lst_s =sorted(set(lst),reverse=True)
lst_c = [lst_s[i] for i in range(3)]

print(lst)
print(lst_c)