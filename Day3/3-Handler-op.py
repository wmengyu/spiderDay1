import urllib.request

#构建handler对象
handler = urllib.request.HTTPHandler()
#通过handler对象构建一个opener对象
opener = urllib.request.build_opener(handler)
url = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}
#构建请求
req = urllib.request.Request(url=url, headers=headers)
#发送请求
res = opener.open(req)
print(res.read().decode('utf-8'))