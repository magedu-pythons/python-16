
#编写一个函数，能够接受至少2个参数，返回最小值和最大值

def rmaxmin(*args):
    max_num = max(args)
    min_num = min(args)
    return print("{}中最小值={},最大值={}".format(args, min_num, max_num))

rmaxmin(3,56,35,1,565,45,897,4568,32254,32335,5556)


#编写一个函数，接受一个参数n, n为正整数，左右两种打印方式。要求数字必须对齐

def sortpractice(n):
    flag = []
    lenght = 0
    c  = ''
    for i in range(1,n+1):
        flag.append(i)
    for k in flag:
        c += "{}{}".format(str(k),' ')
    lenght = len(c)

    for i in range(1,n+1):
        numstem = []
        b =''
        for j in range(1,i+1):
            numstem.insert(0,j)
        for k in numstem:
            b += "{}{}".format(str(k),' ')
        print('{:>{}}'.format(b,lenght))
sortpractice(50)

print('------------我是分割线----------------------------')

def rsortpractice(n):
    flag = []
    lenght = 0
    c  = ''
    for i in range(1,n+1):
        flag.append(i)
    for k in flag:
        c += "{}{}".format(str(k),' ')
    lenght = len(c)

    for i in range(n,0,-1):
        numstem = []
        b =''
        for j in range(1,i+1):
            numstem.insert(0,j)
        for k in numstem:
            b += "{}{}".format(str(k),' ')
        print('{:>{}}'.format(b,lenght))
rsortpractice(50)

print('------------我是分割线----------------------------')

def show(n):
    max_str = " ".join(str(i) for i in range(n,0,-1))
    lenght = len(max_str)

    for i in range(n):
        print('{:>{}}'.format(" ".join(str(j) for j in range(i+1,0,-1)),lenght))


show(12)

print('------------我是分割线----------------------------')

def rshow(n):
    max_str = " ".join(str(i) for i in range(n,0,-1))
    lenght = len(max_str)

    for i in range(n-1,-1,-1):
        print('{:>{}}'.format(" ".join(str(j) for j in range(i+1,0,-1)),lenght))


rshow(12)
