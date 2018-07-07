import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

url = 'https://www.qiushibaike.com/text'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.3'
}

req = urllib.request.Request(url=url, headers=headers)
res = urllib.request.urlopen(req)
#构建bs4
bs = BeautifulSoup(res.read(), 'lxml')
#使用bs4
picurl = bs.select('#content-left a > img')[0]['src']
jobname = bs.select('#content-left h2')[0].string
content = bs.select('#content-left .content > span')[0].get_text()

print(picurl)
print(jobname)
print(content)