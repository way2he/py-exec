# 修正示例
def create_functions():
    funcs = []
    for i in range(3):
        funcs.append(lambda x=i: x*2)  # 通过默认参数绑定当前i值
    return funcs

funcs = create_functions()
for f in funcs:
    print(f())  # 输出0 2 4