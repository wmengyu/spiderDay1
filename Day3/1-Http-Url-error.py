import urllib.request


# url = 'http://www.baidu.com/'
url = 'http://www.baidu-hhh.com/'
#制造HTTPError(不正确的url)
# url = ''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.3'
}
req = urllib.request.Request(url=url, headers=headers)
try:
    res = urllib.request.urlopen(req)
    print(res.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print('1-url-error')
    print(e)
    print(e.code)
    print(e.reason)

except urllib.error.URLError as e:
    print('2-url-error')
    print(e)
except Exception as e:
    print('3-exception')
    print(e)

print('--已经到最后了--')
