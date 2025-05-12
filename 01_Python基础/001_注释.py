# 这是单行注释

"""这里是
多行注释"""

print("hello world")

def add(a, b):
    """计算两个数的和
    参数：
        a (int): 第一个数
        b (int): 第二个数
    返回：
        int: 两数之和
    """
    return a + b

def add2(a: int, b: int) -> int:
    """计算两个整数的和。

    Args:
        a: 第一个整数
        b: 第二个整数

    Returns:
        两个整数的和

    Raises:
        TypeError: 如果输入不是整数
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("参数必须是整数")
    return a + b

print(add2.__doc__)  # 输出文档字符串内容