import urllib.request


url = 'https://www.baidu.com'
#
res = urllib.request.urlopen(url=url)
# print(res)
# print(type(res))
result = res.read().decode('utf-8')
print(result)
