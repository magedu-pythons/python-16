#九九乘法表，反着打

for i in range(1, 10):
    multiplication = ''
    for c in range(i, 10):
        multiplication_Formula = str(i) + '*' + str(c) + '=' + str(c * i)+'\t'
        multiplication += multiplication_Formula
        multiplication1 = '     \t' * (i - 1) + multiplication
        continue
    print(multiplication1)
