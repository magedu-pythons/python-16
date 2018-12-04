'''
本周作业，希望大家认真完成哦（12.3-12.9）
1、请将 "1,2,3"，变成 ["1","2","3"]
2、使用Python copy一个文件，从a目录,copy文件到b目录
3、以下代码输出什么，请解释原因(写到问题下方):
li = [ [ ] ] * 5
li[0].append(10)
print(li)
li[1].append(20)
print(li)
li.append(30)
print(li)
'''
# No.1
strs = "1,2,3"
def dataconversion(strs):
	charStr = list(strs.split(','))
	return charStr

print("string:{}".format(strs))
print("list of char:{}".format(dataconversion(strs)))

# No.2
import pickle
filepath = 'd:\test.log'
def copyfile(filepath):
    with open(filepath,'w') as f1:
        pickle.dump(f1)

# No.3

li = [ [ ] ] * 5
li[0].append(10)
print(li)
li[1].append(20)
print(li)
li.append(30)
print(li)
'''
第一次打印：[[10], [10], [10], [10], [10]],将li列表的list数据元素浅拷贝5次，元素id没变，浅拷贝内容统一追加int数据10
第二次打印：[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]，元素list数据类型ID不变，内容统一尾部追加20
第三次打印：[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]，是给li列表追加新int数据类型30
'''

