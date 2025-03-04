# 生成器
g = (x * x for x in range(10))


#print(g)
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))


# 斐波那契数列
def fibonacci(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    print('done')


fibonacci(6)
