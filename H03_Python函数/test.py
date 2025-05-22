# 计算列表的平均值
def calcAvg(nums):
    return sum(nums) / len(nums)


def calculate_rectangle_area(length, width):
    """计算矩形的面积
    
    Args:
        length (float): 矩形的长度
        width (float): 矩形的宽度
    
    Returns:
        float: 矩形的面积
    """
    return length * width  # 面积 = 长 * 宽


def calculate_composite_area(a, b):
    """计算两个矩形的面积之和
    
    Args:
        a (tuple): 第一个矩形的长和宽（length, width）
        b (tuple): 第二个矩形的长和宽（length, width）
    
    Returns:
        float: 两个矩形的面积之和
    """
    area1 = calculate_rectangle_area(a[0], a[1]) 
    area2 = calculate_rectangle_area(b[0], b[1])  
    return area1 + area2  

print(calcAvg([1, 2, 3, 4, 5]))
print("两个矩形的总面积为：", calculate_composite_area((3, 4), (5, 6)))

"""
请编写一个程序，定义一个元组 student，包含学生的信息，包括姓名、年龄和性别。
然后，使用元组拆包的方式将学生的信息提取出来，并分别存储到对应的变量中。
最后，分别输出学生的姓名、年龄和性别。
"""
# 定义学生信息元组
student = ("张三", 18, "男")

# 元组拆包提取信息（姓名、年龄、性别）
name, age, gender = student

# 输出学生信息
print("学生姓名：", name)
print("学生年龄：", age)
print("学生性别：", gender)

def print_info(name, age, city="未知", gender="未知"):
    """打印人物信息
    
    Args:
        name (str): 姓名（必须）
        age (int): 年龄（必须）
        city (str): 城市（可选，默认'未知'）
        gender (str): 性别（可选，默认'未知'）
    """
    # 按指定格式打印各信息
    print(f"姓名：{name}")
    print(f"年龄：{age}")
    print(f"城市：{city}")
    print(f"性别：{gender}")

# 调用函数，传递不同的参数
print_info("张三", 25, city="北京", gender="女")
print_info("李四", 30, gender="男")

"""
假设你正在开发一个学生成绩管理系统，需要编写 Python 代码来计算学生的总成绩和平均成绩。请完成以下要求：
已知一个学生的成绩列表 scores = [80, 90, 85, 95, 70]，其中每个元素表示学生的一门成绩。请使用函数嵌套调用的方式编写代码，实现以下功能：

创建一个函数 calculate_total(scores)，计算学生的总成绩，并返回结果。
创建一个函数 calculate_average(scores)，计算学生的平均成绩，并返回结果。
在 calculate_average(scores) 函数内部，通过调用 calculate_total(scores) 函数来获取学生的总成绩，并计算平均成绩。
在主程序中调用 calculate_average(scores) 函数，并输出学生的总成绩和平均成绩。
请编写上述要求的代码，并输出学生的总成绩和平均成绩。
"""
def calculate_total(scores):
    """
    计算学生的总成绩

    Args:
        scores (list): 学生的成绩列表

    Returns:
        int: 学生的总成绩

    """
    return sum(scores)

def calculate_average(scores):
    """
    计算平均分数。

    Args:
        scores (list of float): 包含分数的列表。

    Returns:
        float: 列表的平均分数。

    """
    # return sum(scores) / len(scores)
    return calculate_total(scores) / len(scores)

# 主程序调用
scores = [80, 90, 85, 95, 70]
total = calculate_total(scores)
average = calculate_average(scores)
print("学生的总成绩为：", total)
print("学生的平均成绩为：", average)

# 写一个 lambda 表达式，用于将字符串列表中的字符串都转换为大写
uppercase = lambda x: x.upper()
print(uppercase('itheima'))

# 分别定义加减乘除四个函数实现两个数之间的加减乘除操作。
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
# 地板除法（向下取整除法）运算符 // ，计算结果为两个数相除后向下取整的整数
divide = lambda x, y: x // y
# 普通除法运算符 / ，计算结果始终为浮点数（即使能整除）
# divide = lambda x, y: x / y

print(add(1, 2))
print(subtract(3, 1))
print(multiply(2, 3))
print(divide(6, 2))

"""
定义函数findall，要求返回符合要求的所有位置的起始下标，
如字符串"helloworldhellopythonhelloc++hellojava"
需要找出里面所有的"hello"的位置，返回的格式是一个元组，
即：(0,10,21,29)
"""
def findall(target_str):
    """查找字符串中所有'hello'的起始位置
    
    Args:
        target_str (str): 目标字符串
    
    Returns:
        tuple: 所有'hello'的起始位置元组
    """
    positions = []
    # 遍历所有可能的起始位置（避免越界）
    for i in range(len(target_str) - 4):
        if target_str[i:i+5] == 'hello':
            positions.append(i)
    return tuple(positions)

str = "helloworldhellopythonhelloc++hellojava" 
print(findall(str))