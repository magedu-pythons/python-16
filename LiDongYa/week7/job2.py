# 把c盘的文件，copy到f盘。
def copyfile(src, dest):
    with open(src, 'r', encoding = 'utf-8') as f1:
        with open(dest, 'w', encoding = 'utf-8') as f2:
            context = f1.read()
            f2.write(context)
    print('Copy had done!')

copyfile('c:/test.txt', 'f:/test.txt')