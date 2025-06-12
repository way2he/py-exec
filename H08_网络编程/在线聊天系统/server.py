import socket
import threading

def handle_client(client_socket, client_address):
    """
    处理单个客户端连接的函数
    
    Args:
        client_socket: 客户端套接字对象
        client_address: 客户端地址信息
    """
    print(f"客户端 {client_address} 已连接")
    
    try:
        while True:
            # 接收客户端消息
            data = client_socket.recv(1024)
            if not data:
                break
                
            # 解码并打印消息
            message = data.decode('utf-8')
            print(f"来自 {client_address} 的消息: {message}")
            
    except Exception as e:
        print(f"处理客户端 {client_address} 时发生错误: {e}")
    finally:
        # 关闭客户端连接
        client_socket.close()
        print(f"客户端 {client_address} 已断开连接")

def start_server():
    """
    启动服务器的主函数
    """
    # 创建服务器套接字
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 绑定地址和端口
    server.bind(('localhost', 8000))
    
    # 开始监听
    server.listen(5)
    print("服务器已启动，正在监听端口 8000...")
    
    try:
        while True:
            # 接受新的客户端连接
            client_socket, client_address = server.accept()
            
            # 为每个客户端创建新线程
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address)
            )
            client_thread.start()
            
    except KeyboardInterrupt:
        print("\n服务器正在关闭...")
    finally:
        server.close()

if __name__ == "__main__":
    start_server() 