def sum_total(*args):
    """ 接收n个数字, 求这些参数数字的和 """
    sum = 0
    for i in args:
        sum += i
    print(sum)
    return sum


# sum_total(1,2,3,4,5)

def find_odd(*args):
    """ 找出传入的列表或元组的奇数位对应的元素, 并返回一个新的列表 """
    new_list = args[::2]
    print(new_list)
    return new_list


# find_odd(1,2,3,4,5,5,6,7,8)

def practice3(**kwargs):
    """ 检查传入字典的每一个value的长度, 如果大于2, 那么仅保留前两个的长度内容 """
    new_dict = {}
    for k, v in kwargs.items():
        if len(v) > 2:
            v = v[:2]
            new_dict[k] = v
    return new_dict


print(practice3(**{'key': 'afdawera', "name": 'yeming'}))
