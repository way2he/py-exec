import time
from functools import wraps  # 新增：用于保留被装饰函数的元信息


def log_time(func):
    """
    装饰器：测量并打印被装饰函数的执行时间
    Args:
        func (function): 被装饰的目标函数
    Returns:
        function: 包装后的函数
    """
    @wraps(func)  # 关键优化：保留原函数元信息
    def wrapper(*args, **kwargs):
        """
        包装函数：执行时间测量逻辑
        Args:
            *args: 目标函数的位置参数
            **kwargs: 目标函数的关键字参数
        Returns:
            目标函数的返回值
        """
        # 记录开始时间
        start = time.perf_counter()
        # 调用目标函数，并传入参数
        result = func(*args, **kwargs)
        # 记录结束时间
        end = time.perf_counter()
        # 打印函数执行耗时
        print(f"{func.__name__}执行耗时：{end - start:.6f}s")
        # 返回目标函数的返回值
        return result
    return wrapper


@log_time
def heavy_compute(*args, **kwargs):
    sum = 0
    for lst in args:
        for i in lst:
            sum += int(i) if isinstance(i, str) and i.isdigit() else i
    for d in kwargs.values():
        for i in d.values():
            sum += int(i) if isinstance(i, str) and i.isdigit() else i
    return sum


print("结果：", heavy_compute([1, 2, 3, 4], {'1':1, '2':2, '3':3, '4':4}))  