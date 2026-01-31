from blocking_queue import BlockingQueue
import threading
import time


def producer(queue: BlockingQueue[int], producer_id: int) -> None:
    """
    生产者线程函数
    
    Args:
        queue: 阻塞队列实例
        producer_id: 生产者ID
    """
    for i in range(5):
        item = producer_id * 100 + i
        print(f"生产者{producer_id}: 尝试放入 {item}")
        queue.put(item)
        print(f"生产者{producer_id}: 成功放入 {item}, 当前队列大小: {queue.size()}")
        time.sleep(0.1)


def consumer(queue: BlockingQueue[int], consumer_id: int) -> None:
    """
    消费者线程函数
    
    Args:
        queue: 阻塞队列实例
        consumer_id: 消费者ID
    """
    for _ in range(5):
        print(f"消费者{consumer_id}: 尝试取出元素")
        item = queue.take()
        print(f"消费者{consumer_id}: 成功取出 {item}, 当前队列大小: {queue.size()}")
        time.sleep(0.15)


def test_basic_usage() -> None:
    """
    测试基本使用场景
    """
    print("=== 测试基本使用 ===")
    queue: BlockingQueue[int] = BlockingQueue[int](capacity=3)
    
    # 测试基本操作
    queue.put(1)
    queue.put(2)
    queue.put(3)
    
    print(f"队列大小: {queue.size()}")
    print(f"是否已满: {queue.is_full()}")
    
    print(f"取出: {queue.take()}")
    print(f"取出: {queue.take()}")
    print(f"队列大小: {queue.size()}")
    print(f"是否为空: {queue.is_empty()}")


def test_timeout() -> None:
    """
    测试超时机制
    """
    print("\n=== 测试超时机制 ===")
    queue: BlockingQueue[int] = BlockingQueue[int](capacity=1)
    
    # 测试offer超时
    queue.put(1)
    print(f"队列已满: {queue.is_full()}")
    
    result = queue.offer(2, timeout=1)
    print(f"尝试放入元素(超时1秒): {result}")
    
    # 测试poll超时
    item = queue.poll(timeout=1)
    print(f"取出元素: {item}")
    
    item = queue.poll(timeout=1)
    print(f"再次取出(超时1秒): {item}")


def test_producer_consumer() -> None:
    """
    测试生产者-消费者模型
    """
    print("\n=== 测试生产者-消费者模型 ===")
    queue: BlockingQueue[int] = BlockingQueue[int](capacity=3)
    
    # 创建生产者和消费者线程
    producers = [threading.Thread(target=producer, args=(queue, i)) for i in range(2)]
    consumers = [threading.Thread(target=consumer, args=(queue, i)) for i in range(2)]
    
    # 启动所有线程
    for p in producers:
        p.start()
    for c in consumers:
        c.start()
    
    # 等待所有线程完成
    for p in producers:
        p.join()
    for c in consumers:
        c.join()
    
    print("所有线程执行完成")


def test_exception_handling() -> None:
    """
    测试异常处理
    """
    print("\n=== 测试异常处理 ===")
    
    # 测试容量异常
    try:
        queue: BlockingQueue[int] = BlockingQueue[int](capacity=0)
    except ValueError as e:
        print(f"捕获到容量异常: {e}")
    
    # 测试None元素异常
    queue = BlockingQueue[int](capacity=5)
    try:
        queue.put(None)
    except TypeError as e:
        print(f"捕获到None元素异常: {e}")


if __name__ == "__main__":
    test_basic_usage()
    # test_timeout()
    # test_exception_handling()
    # test_producer_consumer()
