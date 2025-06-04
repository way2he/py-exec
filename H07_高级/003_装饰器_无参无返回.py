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
    def wrapper():
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
        func()
        # 记录结束时间
        end = time.perf_counter()
        # 打印函数执行耗时
        print(f"{func.__name__}执行耗时：{end - start:.6f}s")
    return wrapper


@log_time
def compute():
    time.sleep(3)


compute() 