li = [ [ ] ] * 5
li[0].append(10)
print(li)
li[1].append(20)
print(li)
li.append(30)
print(li) 

#输出[[10], [10], [10], [10], [10]]
#    [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
#    [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]
#原因：第一行代码[[]]，外面那个列表指向内存中的第一个区域，里面嵌套的列表指向内存
#中的第二个区域，当对里面的元素进行复制时，嵌套列表指向的都是同一个内存区域，因此
#其中一个元素，其他的元素也会改变，而对外层列表追加元素时，是开辟了一块新的内存
#区域