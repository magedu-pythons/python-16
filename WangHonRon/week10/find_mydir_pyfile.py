import os

# 函数查找文件方法：
def find_dir_file(dirc,filesuffix,filelst=None):
    """
    find your directory for file of suffix
    :param dirc: finded directory
    :param filesuffix: file suffix
    :param filelst:
    :return: file list
    """
    if filelst == None:
        filelst = []
    abspath = os.path.abspath(dirc)

    for f in os.listdir(abspath):
        #拼接文件或文件夹目录
        absf = os.path.abspath(os.path.join(abspath,f))

        if os.path.isfile(absf) and absf.endswith(filesuffix):
            filelst.append(absf)
        elif os.path.isdir(absf):
            #递归查找
            find_dir_file(absf,filesuffix,filelst)

    return filelst

print(find_dir_file('D:\TEST-WON','.py'))
