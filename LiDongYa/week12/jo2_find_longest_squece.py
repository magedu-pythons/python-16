'''
给出一个无序的整型列表，找出最长连续元素序列的长度，时间复杂度要求在线性时间内。
例如：
    输入：[8,1,9,3,2,4]，那么其最长连续序列是[1,2,3,4]，即输出长度为4
'''


# 方法一：利用赋值引用性质。
def find_longest_squece1(src):
    value_set = set()   # 存放元素
    value_dict = {}     # 存放元素和标记的键值对
    for i in src:
        if i not in value_set:
            value_set.add(i)    
            value_dict[i] = [1]   # 添加标记记录连续序列的元素个数，利用赋值引用的性质，一个标记改变，其他跟随改变
            if i+1 in value_set and i-1 in value_set:   # 当前后元素都存在时
                value_dict[i+1][0] = value_dict[i+1][0] + 2  # 更新标记，元素个数增2
                value_dict[i] = value_dict[i+1]
                value_dict[i-1] = value_dict[i+1]
            elif i-1 in value_set:  # 只存在前一个元素时
                value_dict[i-1][0] = value_dict[i-1][0] + 1
                value_dict[i] = value_dict[i-1]
            elif i+1 in value_set:  # 只存在后一个元素时
                value_dict[i+1][0] = value_dict[i+1][0] + 1
                value_dict[i] = value_dict[i+1]
    return max(value_dict.values(), key=lambda x:x[0])[0]


# 方法二：遍历元素，用序列最小值叠加1，判断，获得最长序列
def find_longest_squece2(src):
    max_count = 0
    src = set(src)  # hash
    for i in src:
        if i-1 not in src:  # 序列最小值进入
            num = i + 1
            while True:
                num += 1
                if num not in src:
                    break
            max_count = max(max_count, num-i)
    return max_count
