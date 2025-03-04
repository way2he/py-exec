# 迭代器
# 凡是可作用于for循环的对象都是Iterable类型；
#
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
from collections.abc import Iterator
print(isinstance((x * x for x in range(10)), Iterator))

print(isinstance([], Iterator))
print(isinstance({}, Iterator))

print(abs(-1))