#ip代理
import urllib.request

url = 'https://www.baidu.com/s?ie=utf-8&wd=ip'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}

req = urllib.request.Request(url=url,headers=headers)

#配置代理
handler = urllib.request.ProxyHandler({'https':'119.188.162.165:8081'})

#创建opener对象
opener = urllib.request.build_opener(handler)

#发送请求
res = opener.open(req)

with open('id_dl.html', 'wb') as fw:
    fw.write(res.read())