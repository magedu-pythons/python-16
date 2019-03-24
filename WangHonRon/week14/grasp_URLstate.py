# 1、并发抓取10 个url，并且打印出它们的状态码、和文本内容
import requests
import threading

def fetch(urls: list):
    def req(url):
        ret = requests.get(url)
        print(ret.status_code)
        print(ret.content)

    for loc in urls:
        req(loc)
        threading.Thread(target=req, args=(loc,))

if __name__ == '__main__':
    urls = ['http://www.baidu.com','http://www.jd.com','http://www.taobao.com']
    fetch(urls)