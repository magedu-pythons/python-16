#九九乘法表

for i in range(1, 10):
    multiplication = ''
    for c in range(1, i+1):
        multiplication_Formula = str(c) + '*' + str(i) + '=' + str(c * i)+'\t'
        multiplication += multiplication_Formula
    print(multiplication)



