# 自定义函数
import math


def cus_abs(x):
    return abs(x)


print(cus_abs(-10))


# 空函数
def empty_func():
    pass


def two_ret(a, b):
    return a + b, a - b


print(two_ret(1, 2))


def quadratic(a, b, c):
    """
    求解一元二次方程 ax² + bx + c = 0 的根
    返回：包含两个解的元组（支持实数和复数）
    """
    if a == 0:
        raise ValueError("系数a不能为0（非二次方程）")

    discriminant = b ** 2 - 4 * a * c  # 更高效的写法
    sqrt_d = math.sqrt(discriminant)
    denominator = 2 * a  # 分母复用避免重复计算
    root1 = (-b - sqrt_d) / denominator
    root2 = (-b + sqrt_d) / denominator
    return root2, root1


def quadratic2(a, b, c):
    m = b ** 2 - 4 * a * c;
    return ((-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
            , (-b - math.sqrt(m)) / (2 * a))


# 测试:
print('quadratic(2, 3, 1) =', quadratic2(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic2(1, 3, -4))

if quadratic2(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic2(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
