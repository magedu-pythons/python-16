# 2、实现一个wsgi的http web服务端
from wsgiref.simple_server import make_server

def app(environ, start_response):
    headers = {'Content-Type': 'text/plain; charset=utf-8'}
    start_response('200 OK', list(headers.items()))

    yield 'Hi python! \r\n'.encode('utf-8')

if __name__ == '__main__':
    httpd = make_server('127.0.0.1', 8081, app)
    host, port = httpd.socket.getsockname()
    print(host, port)
    httpd.serve_forever()
