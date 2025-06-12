# 定义外部函数 outer
def outer():
    # 在外部函数作用域中定义变量 num
    num = 5

    # 定义内部函数 inner
    def inner():
        # 使用 nonlocal 关键字声明 num 不是局部变量，而是外部函数的变量
        nonlocal num
        # 修改外部函数作用域中的 num 变量
        num = num * 2  # 核心逻辑：修改外部变量
        # 返回修改后的 num 值
        return num

    # 外部函数返回内部函数对象
    return inner

# 调用外部函数 outer()，并将返回的内部函数对象赋值给 func
func = outer()
# 调用内部函数 func()，执行 num = num * 2 的操作
result = func()
# 打印内部函数执行后的结果
print(result) 