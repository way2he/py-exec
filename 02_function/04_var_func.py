# 可变参数函数

def calc(*numbers):
    sums = 0
    for n in numbers:
        sums = sums + n
    return sums


print(calc(1, 2, 3, 4, 5, 6))
print(calc(1, 2, 3))