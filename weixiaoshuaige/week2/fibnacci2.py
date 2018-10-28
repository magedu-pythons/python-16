fibs = [1, 1]
for i in range(100):
    val = fibs[i] + fibs[i + 1]
    if val >= 100:
        break
    else:
        fibs.append(val)
print(fibs)