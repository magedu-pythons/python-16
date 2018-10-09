# 求10万以内质数
import datetime
start = datetime.datetime.now()
count = 0
for num2 in range(2, 100000):
    for i in range(2, int(num2 ** 0.5) + 1):
        if num2 % i == 0:
                break
    else:
        print(num2)
        count += 1
end = (datetime.datetime.now() - start).total_seconds()

print(count)
print(end)
