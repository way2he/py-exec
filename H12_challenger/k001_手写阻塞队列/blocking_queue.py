import threading
from typing import Generic, TypeVar, Optional
from collections import deque
import time


T = TypeVar('T')


class BlockingQueue(Generic[T]):
    """
    线程安全的阻塞队列实现
    
    特性：
    1. 当队列为空时，take()操作会阻塞直到有元素可用
    2. 当队列已满时，put()操作会阻塞直到有空间可用
    3. 支持超时机制
    4. 线程安全，使用条件变量实现同步
    """
    
    def __init__(self, capacity: int = 10):
        """
        初始化阻塞队列
        
        Args:
            capacity: 队列最大容量，必须大于0
            
        Raises:
            ValueError: 当capacity小于等于0时抛出
        """
        if capacity <= 0:
            raise ValueError(f"队列容量必须大于0，当前值: {capacity}")
        
        self._queue: deque[T] = deque()
        self._capacity: int = capacity
        self._lock: threading.Lock = threading.Lock()
        self._not_empty: threading.Condition = threading.Condition(self._lock)
        self._not_full: threading.Condition = threading.Condition(self._lock)
    
    def put(self, item: T, timeout: Optional[float] = None) -> bool:
        """
        将元素放入队列，如果队列已满则阻塞直到有空间可用
        
        Args:
            item: 要放入的元素
            timeout: 超时时间（秒），None表示无限等待
            
        Returns:
            bool: 成功放入返回True，超时返回False
            
        Raises:
            TypeError: 当item为None时抛出
        """
        if item is None:
            raise TypeError("不允许放入None元素")
        
        with self._not_full:
            # 队列已满，等待有空间
            if len(self._queue) >= self._capacity:
                if timeout is None:
                    # 无限等待
                    while len(self._queue) >= self._capacity:
                        self._not_full.wait()
                else:
                    # 带超时的等待
                    end_time = time.time() + timeout
                    while len(self._queue) >= self._capacity:
                        remaining = end_time - time.time()
                        if remaining <= 0:
                            return False
                        self._not_full.wait(remaining)
            
            # 放入元素
            self._queue.append(item)
            
            # 通知可能等待的消费者
            self._not_empty.notify()
            
            return True
    
    def take(self, timeout: Optional[float] = None) -> Optional[T]:
        """
        从队列取出元素，如果队列为空则阻塞直到有元素可用
        
        Args:
            timeout: 超时时间（秒），None表示无限等待
            
        Returns:
            Optional[T]: 取出的元素，超时返回None
        """
        with self._not_empty:
            # 队列为空，等待有元素
            if len(self._queue) == 0:
                if timeout is None:
                    # 无限等待
                    while len(self._queue) == 0:
                        self._not_empty.wait()
                else:
                    # 带超时的等待
                    end_time = time.time() + timeout
                    while len(self._queue) == 0:
                        remaining = end_time - time.time()
                        if remaining <= 0:
                            return None
                        self._not_empty.wait(remaining)
            
            # 取出元素
            item = self._queue.popleft()
            
            # 通知可能等待的生产者
            self._not_full.notify()
            
            return item
    
    def offer(self, item: T, timeout: Optional[float] = None) -> bool:
        """
        尝试将元素放入队列，如果队列已满则阻塞指定时间
        
        Args:
            item: 要放入的元素
            timeout: 超时时间（秒），None表示不等待
            
        Returns:
            bool: 成功放入返回True，失败返回False
        """
        if item is None:
            raise TypeError("不允许放入None元素")
        
        return self.put(item, timeout)
    
    def poll(self, timeout: Optional[float] = None) -> Optional[T]:
        """
        尝试从队列取出元素，如果队列为空则阻塞指定时间
        
        Args:
            timeout: 超时时间（秒），None表示不等待
            
        Returns:
            Optional[T]: 取出的元素，失败返回None
        """
        if timeout is None:
            timeout = 0
        return self.take(timeout)
    
    def size(self) -> int:
        """
        获取队列当前元素数量
        
        Returns:
            int: 队列中的元素数量
        """
        with self._lock:
            return len(self._queue)
    
    def is_empty(self) -> bool:
        """
        判断队列是否为空
        
        Returns:
            bool: 队列为空返回True，否则返回False
        """
        with self._lock:
            return len(self._queue) == 0
    
    def is_full(self) -> bool:
        """
        判断队列是否已满
        
        Returns:
            bool: 队列已满返回True，否则返回False
        """
        with self._lock:
            return len(self._queue) >= self._capacity
    
    def remaining_capacity(self) -> int:
        """
        获取队列剩余容量
        
        Returns:
            int: 剩余可用容量
        """
        with self._lock:
            return self._capacity - len(self._queue)
    
    def clear(self) -> None:
        """
        清空队列
        """
        with self._lock:
            self._queue.clear()
            # 通知所有等待的生产者
            self._not_full.notify_all()
