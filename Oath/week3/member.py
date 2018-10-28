def member(x:int, lst:list=None) -> int:
    ''' This is a function......
    :param x:int
    :param lst:list
    :return: int
    '''
    if not lst:
        lst = []
    if x in lst:
        return 1
    return 0
newlst = [i**0.5 for i in range(99)]
print(member(18, newlst))