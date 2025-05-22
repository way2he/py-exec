def fun(*args, **kwargs):
    """
    计算不定长参数中列表数字元素与字典value值的累积和
    :param args: 包含任意数量列表的不定长参数
    :param kwargs: 包含任意数量字典的关键字参数
    :return: 所有数字元素的累积和
    """
    total = 0
    # 处理列表参数（args中的每个元素应为列表）
    for arg in args:
        if isinstance(arg, list):  # 确保参数是列表类型
            for num in arg:
                if isinstance(num, (int, float)):  # 仅累加数字类型
                    total += num
    # 处理字典参数（kwargs中的每个值应为字典）
    for value in kwargs.values():
        if isinstance(value, dict):  # 确保参数是字典类型
            for v in value.values():
                if isinstance(v, (int, float)):  # 仅累加数字类型
                    total += v
    return total

if __name__ == "__main__":
    # 示例调用
    result = fun([1, 2, 3], my_dict={'a': 4, 'b': 5, 'c': 6})
    print(f"累积结果为：{result}")  # 输出：累积结果为：21