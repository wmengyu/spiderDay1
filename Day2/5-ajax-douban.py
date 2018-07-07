import urllib.request
import urllib.parse

url = 'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action=&'
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'

}
page = int(input('请输入要查看的页码; '))
start = (page-1)*20
limit = 20

data={
    'start':start,
    'limit':limit
}

data = urllib.parse.urlencode(data).encode('utf-8')
#构建路径(get请求)
# url += data
#构建请求(post请求)
req = urllib.request.Request(url=url, data=data, headers=headers)
#发送请求
res = urllib.request.urlopen(req)
# print(res.read().decode('utf-8'))


with open('douban.html', 'wb') as fw:
    fw.write(res.read())
