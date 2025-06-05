import socket

def tcp_server(host='127.0.0.1', port=8888):
    # 创建TCP套接字（AF_INET表示IPv4，SOCK_STREAM表示TCP）
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))  # 绑定地址和端口
        s.listen(5)  # 监听连接，最大排队数5
        print(f"TCP服务器启动，监听{host}:{port}")
        while True:
            conn, addr = s.accept()  # 阻塞等待客户端连接
            with conn:
                print(f"客户端{addr}已连接")
                while True:
                    data = conn.recv(1024)  # 接收最多1024字节数据
                    if not data:
                        break
                    conn.sendall(data.upper())  # 响应大写数据

if __name__ == '__main__':
    tcp_server()