
def copy_file(src, desc):
    with open(src) as f1:
        with open(desc, "w") as f2:
            f2.write(f1.read())

copy_file("readme.txt", "copy.txt")

"""
(0 + 0)

    参考答案的更好实现
"""