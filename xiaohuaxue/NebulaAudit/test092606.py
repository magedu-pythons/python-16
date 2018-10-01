for i in range(1, 10):
    multiplication = ''
    for j in range(i, 10):
        multiplication += "{}*{}={:<{}}  ".format(i, j, i*j, 2 if j < 4 else 3)
    print("{:>80}".format(multiplication))
