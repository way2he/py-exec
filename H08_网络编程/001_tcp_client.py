import socket

def tcp_client(host='127.0.0.1', port=8888):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))  # 连接服务器
        s.sendall(b'Hello, TCP!')  # 发送数据
        data = s.recv(1024)  # 接收响应
        print(f"接收响应：{data.decode()}")

if __name__ == '__main__':
    tcp_client()