#自定义请求
import urllib.request

url= 'http://www.baidu.com'
# res=urllib.request.urlopen(url=url)
# print(res.getheaders())

headers = {
 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}

#构建请求 - 第1种方式
# req=urllib.request.Request(url=url,headers=headers)

#构建请求 - 第2种方式(实际分为2步)
req=urllib.request.Request(url=url)
req.add_header("User-Agent","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36")

# 发送请求
res=urllib.request.urlopen(req)

print(res.read().decode('utf-8'))