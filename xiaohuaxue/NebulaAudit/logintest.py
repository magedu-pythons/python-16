
#形参设置默认值，即缺省值。  缺省值往往都会用，特别参数超过3,4个以上，一般都要有缺省值
def login(host='127.0.0.1',port='8080',username='wayne',password='magedu'):
    print('{}:{}@{}/{}'.format(host,port,username,password))

login()

login('127.0.0.2',80,'tom','tom')

login('127.0.0.3',username='root')

login('localhost',port=80,password='com')

login(port=80,password='magedu2',host='www')

print('end-------------------------')