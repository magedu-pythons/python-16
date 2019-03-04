# 12、将"1,2,3"变成["1", "2", "3"]
import re
m_str = "1,2,3"
#m_str = "1.2,3"
#m_str = "1'2,3"
def str2lst(m_str:str):
    regex = re.compile('[^\w]')
    return regex.split(m_str)
print(str2lst(m_str))
#
str2lst=lambda m_str:m_str.split(',')
print(str2lst(m_str))


# 13、使用Python copy一个文件，从a目录，copy文件到b目录
import shutil
from pathlib import Path
def cpfile(src, dst):
    src = Path(src)
    dst = Path(dst)
    if not src.exists():
        raise FileNotFoundError('{} is not exist'.format(src))
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
src = 'test'
dst = 'D:hy/12323/test1'
cpfile(src, dst)


"""
(0 + 0)

    基本上没问题！
"""