# 服务器端示例代码
import socket

def start_server():
    # 创建服务器套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定地址和端口
    server_socket.bind(('localhost', 8080))
    # 开始监听
    server_socket.listen(5)
    
    while True:
        # 接受客户端连接
        client_socket, address = server_socket.accept()
        # 接收数据
        data = client_socket.recv(1024)
        # 发送响应
        client_socket.send(b'Hello from server!')
        # 关闭连接
        client_socket.close()