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
    def wrapper(n):
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
        result = func(n)
        # 记录结束时间
        end = time.perf_counter()
        # 打印函数执行耗时
        print(f"{func.__name__}执行耗时：{end - start:.6f}s")
        # 返回目标函数的返回值
        return result
    return wrapper


@log_time
def heavy_compute(n):
    """
    计算0到n-1的平方和（优化后使用数学公式）
    Args:
        n (int): 计算上限（不包含n）
    Returns:
        int: 平方和结果
    """
    # 优化：将O(n)的生成器计算改为O(1)的数学公式
    return (n-1) * n * (2*n - 1) // 6


print("结果：", heavy_compute(1000000))  # 输出示例：heavy_compute执行耗时：0.000002s（性能显著提升）