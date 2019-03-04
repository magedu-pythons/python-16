"""
已知仓库中有若干商品，以及相应库存，类似：
袜子，10
鞋子，20
拖鞋，30
项链，40
要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数
"""

# 思路：为每件商品进行编号，每件商品都是独立的存在，放入集合中，随机从集合中获取样品
import random

commodities = ['socks', 'shoes', 'slippers', 'necklace']
number = [10, 20, 30, 40]

# 把编号的商品放入集合中，
s = {k for i, item in enumerate(commodities) for k in zip([item] * number[i], range(number[i]))}


# 获取商品函数
def getcommodity():
    """
    获取商品函数，单次单拿，商品被返回的概率与其库存成正比
    """
    # 仓库有货时
    if s:
        commodity = random.sample(s, 1)  # 从仓库中获取一种商品，商品概率与其库存成正比
        s.discard(commodity[0])          # 从仓库中减去被取走的商品
        return commodity[0][0]
    # 仓库无货时
    else:
        return None


# 执行函数
def main():
    getnumber = int(input("请输入获取商品的个数："))
    while getnumber:
        commodity = getcommodity()
        if commodity:
            print('获得商品{}'.format(commodity))
        else:
            print('仓库已经空了！')
            break
        getnumber -= 1


if __name__ == '__main__':
    main()

"""
(0 + 0)


"""