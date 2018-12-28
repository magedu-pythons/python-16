#!/usr/bin/env python
"""
1请将“1,2,3”，变成["1","2","3"]
"""
def func():
    astring="1,2,3"
    sets=lambda "x","y","z":[]



#使用python copy一个文件，从a目录copy文件到b目录
#先判断目录存在不，存在在判断文件，否则创建
import os
import shutil
def sourcefile(src,des):
    src=os.path.normpath("/a/file1")
    des=os.path.normpath("/b/")
    if not os.path.exists("/a") or not os.path.exists(des):
        print("文件路径不存在")
        os.mkdir("/a/")
        os.mkdir("des")
        if os.path.isfile (src):
            shutil.copy (src, des)
            print (" copy Success")
        else:
            os.mkdir(src)
            shutil.copy (src, des)
            print (" copy Success")
    else:
        shutil.copy (src, des)
        print( " copy Succes")

#目前还有点问题，函数用的不好，还待改进


#3以下代码输出什么，请解释原因
li=[[]]*5
li[0].append(10)
print(li)

#Answer
"""[[10], [10], [10], [10], [10]]
[[], [], [], [], []]
这个就相当于一个空列表的嵌套，[]数值为None,做了一个类型转换，与相乘10
"""
li[1].append(20)
print(li)


#Answer
"""[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]

list[0]是10，list[1]站位20
"""


li[1].append(30)
print(li)

#[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]


"""
(0 + 0)

    格式比较乱，建议参考答案的形式修正
"""