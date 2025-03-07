# 过滤器

# 在一个list中，删掉偶数，只保留奇数

def filter_num(n):
    # return n % 2 == 0
    return n % 2 == 1


print(list(filter(filter_num, range(1, 11))))


# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))