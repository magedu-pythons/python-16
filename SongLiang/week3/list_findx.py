import random
lst = [random.randint(1,20) for n in range(10)]
print(lst)
x = int(input('(1~~20)>>>'))
print(1) if x in lst else print(0)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import random
lst = [random.randint(1,20) for n in range(10)]
x = int(input('(1~~20)>>>'))
try:
    lst.index(x)
except ValueError:
    print(0)
else:
    print(1)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import random
lst = [random.randint(1,20) for n in range(10)]
x = int(input('(1~~20)>>>'))
num = lst.count(x)
print(0) if num == 0 else print(1)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import random
lst = [random.randint(1,20) for n in range(10)]
x = int(input('(1~~20)>>>'))
for i in lst:
    if x == i:
        print(1)
        break
else:
    print(0)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import random
lst = [random.randint(1,20) for n in range(10)]
x = int(input('(1~~20)>>>'))
try:
    lst.remove(x)
except ValueError:
    print(0)
else:
    print(1)

"""
(0 + 0)

    python中注释使用#号,不然报语法错误
"""