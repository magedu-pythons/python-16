"""
socket server
"""
import socket

def my_server():
    # 创建 server socket对象
    soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 访问地址
    server_address = ('127.0.0.1', 8082)
    # 绑定本地地址和端口
    soket.bind(server_address)
    # 监听
    soket.listen(1)
    while True:

        conn, client_address = soket.accept()
        try:
            print('connection from', client_address)

            while True:

                data = conn.recv(1024)
                if data:

                    print("client Data: {}".format(data))
                    resp = '{} {} {}'.format(data, *client_address)
                    conn.send(resp.encode())
                if data.decode() == 'quit':

                    print("no data，being quit")
                    break
        finally:
            conn.close()


socket_server = my_server()