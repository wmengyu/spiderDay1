import os
import urllib.parse
import urllib.request

def download(req, page):
    res = urllib.request.urlopen(req)
    dirname = 'tieba'
    filename = '第' + str(page)+"页.html"
    filepath = os.path.join(dirname, filename)
    with open(filepath, 'wb') as fw:
        fw.write(res.read())

#拼接url构建请求对象
def build_url(url, page, tname):
    #拼接url
    pn = (page-1)*50
    data={
        'kw':tname,
        'pn': pn
    }
    data = urllib.parse.urlencode(data)
    url += data
    req = urllib.request.Request(url=url)
    return req

def main():
    start_page = int(input("请输入起始页码: "))
    end_page = int(input("请输入结束页码: "))
    tname = input("请输入贴吧名: ")
    url = 'http://tieba.baidu.com/f?&ie=utf-8&'
    for page in range(start_page, end_page+1):
        req = build_url(url, page, tname)
        download(req, page)

if __name__ == '__main__':
    main()