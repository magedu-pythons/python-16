from pathlib import Path

# 文件查找函数
def find_pyfile(path:Path):
    if path.is_dir():
        lst = []
        for i in path.glob('**/*.py'):
            lst.append(i.name)
        print('Pyfile is {}'.format(lst))
    else:
        print('Error path!')


# 交互函数
def main():
    p = input('Plz input your path:')
    path = Path(p)
    find_pyfile(path)


if __name__ == '__main__':
    main()