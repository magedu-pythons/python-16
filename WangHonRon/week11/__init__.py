"""
第十一周作业班主任-薇薇 1月2号 星期三 14:59
新年好呀各位来波新作业，本周作业如下：(1.2-1.6)
本周作业如下：
1、实现数据结构stack(栈)，并实现它的append，pop方法【动手查询相关资料理解stack特点以及与queue区别】
2、打印出N对合理的括号组合。
例如： 当N=3，输出：()()(),()(()),(())(),((()))
3、根据字典，从一个抹去空格的字符串里面提取出全部单词组合，并且拼接成正常的句子:
例如: 输入一个字符串："thisisanexample", 程序输出: "this is an example"

    深度优先搜索，对单词字符串进行迭代，
    查看是否在字典集合中，找到后，对剩下的字符进行递归调用
    :param inputs: 输入的字符串
    :param word_set: 单词字典
    :param memorized: 缓存字典，用来记忆化搜索，加速计算
    :return:

"""

