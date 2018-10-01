import datetime
import math
start = datetime.datetime.now()
lst = []
flag = False
for num2 in range(2, 100000):
        for i in lst:
            if num2 % i == 0:
                flag = True
                break
            if i >= math.ceil(num2 ** 0.5):
                flag = False
                break
        if not flag:
            print(num2)
            lst.append(num2)
end = (datetime.datetime.now() - start).total_seconds()
print(len(lst))
print(end)


