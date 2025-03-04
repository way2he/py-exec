from collections.abc import Iterable

for i in 'abc':
    print(i)

print(isinstance('abc', Iterable))
print(isinstance([123], Iterable))
print(isinstance(123, Iterable))

for key, value in enumerate(['a', 'b', 'c']):
    print(key, value)


def findMinAndMax(L):
    min_s = 0
    max_s = 0
    for i in L:
        if i < min_s:
            min_s = i
        elif i > max_s:
            max_s = i
    return min_s, max_s


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
