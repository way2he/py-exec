# 发送端（udp_sender.py）import socket

def udp_sender(host='<broadcast>', port=9999):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # 启用广播
        message = b'Hello, UDP Broadcast!' 
        s.sendto(message, (host, port))  # 向广播地址发送
        print("广播消息已发送")

if __name__ == '__main__':
    udp_sender()