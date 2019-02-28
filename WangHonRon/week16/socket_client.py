"""
socket client
"""
import socket

def my_client(ip, port, msg):
    # 实例化客户端socket
    clit_socket = socket.socket()

    # client 和 server 端建立连接
    clit_socket.connect((ip, port))

    # client 给 server 端发送消息
    clit_socket.send(msg.encode())

    # client 接收 server 响应的信息
    resp = clit_socket.recv(1024)
    print(resp)

if __name__ == '__main__':
    raddrIP = '127.0.0.1'
    raddrPort = 8082
    mess = 'How are you ? I am from client of Python socket'
    myclient = my_client(raddrIP,raddrPort,mess)