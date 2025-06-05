import socket

def udp_receiver(host='', port=9999):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))  # 绑定任意地址
        print("UDP接收端启动，等待消息...")
        while True:
            data, addr = s.recvfrom(1024)  # 接收数据和发送方地址
            print(f"来自{addr}的消息：{data.decode()}")

if __name__ == "__main__":
    udp_receiver()  # 默认监听所有网络接口的9999端口