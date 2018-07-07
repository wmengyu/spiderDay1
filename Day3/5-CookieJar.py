
import http.cookiejar
import urllib.request
import urllib.parse
#创建一个cookiejar对象
cookie = http.cookiejar.CookieJar()
#通过Cookiejar 对象生成handler对象
handler = urllib.request.HTTPCookieProcessor(cookie)
#通过handler对象生成opener对象
opener = urllib.request.build_opener(handler)

url = ''
data = {
    'username':'15971173880',
    'password':'36573880my',
    'savestate':'1',
    'r':'http%3A%2F%2Fweibo.cn%2F',
    'ec':'0',
    'pagerefer':'',
    'entry':'',
    'mweibo':'',
    'wentry':',',
    'loginfrom':'',
    'client_id':'',
    'code':'',
    'qq':'',
    'mainpageflag':'1',
    'vid':'dbceb896cc475c70895772bb00c8ce5d91b00c8ce5d9',
    'hff':'',
    'hfp':''
}

data = urllib.parse.urlencode(data).encode('utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://weibo.com',
    'Host': 'login.sina.com.cn',
    'Connection': 'keep-alive',
    'Referer': 'https://weibo.com/',
    'Accept': '*/*'
}

req = urllib.request.Request(data=data, url=url, headers=headers)
res = opener.open(req)
print(res.read().decode('gbk'))


url = ''

headers1={

}

req1 = urllib.request.Request(url=url, headers=headers1)
res1 = opener.open(req1)
print(res1.read().decode('gbk'))
