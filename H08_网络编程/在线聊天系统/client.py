import socket

def send_message(message):
    """
    向服务器发送消息的函数
    
    Args:
        message: 要发送的消息字符串
    """
    # 创建客户端套接字
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # 连接到服务器
        client.connect(('localhost', 8000))
        
        # 将消息编码为字节串并发送
        client.sendall(message.encode('utf-8'))
        print(f"消息已发送: {message}")
        
    except Exception as e:
        print(f"发送消息时发生错误: {e}")
    finally:
        # 关闭连接
        client.close()

def main():
    """
    主函数，处理用户输入并发送消息
    """
    print("欢迎使用聊天客户端！")
    print("输入 'quit' 退出程序")
    
    while True:
        # 获取用户输入
        message = input("请输入要发送的消息: ")
        
        # 检查是否退出
        if message.lower() == 'quit':
            print("正在退出程序...")
            break
            
        # 发送消息
        send_message(message)

if __name__ == "__main__":
    main() 