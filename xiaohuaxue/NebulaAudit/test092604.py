import datetime
start = datetime.datetime.now()
count = 1
for num2 in range(3, 100000, 2):
        for i in range(3, int(num2 ** 0.5) + 1, 2):
            if num2 % i == 0:
                break
        else:
            print(num2)
            count += 1
end = (datetime.datetime.now() - start).total_seconds()
print(count)
print(end)
