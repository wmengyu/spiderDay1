import urllib.request
import urllib.parse
import os
import re

#下载
def download_img(img_url):
    dir_path = './qiubai'
    #获得基本文件名
    img_name = os.path.basename(img_url)
    file_path = os.path.join(dir_path, img_name)
    #下载
    urllib.request.urlretrieve(img_url, file_path)
    print(file_path+'下载完毕')

#获取内容
def get_content(req):
    #发送请求
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf-8')
    #通过正则拿到图片链接
    pattern = re.compile(r'<div class="thumb">.*?<img src=(.*?) alt=.*?>.*?</div>', re.S)
    src_list = pattern.findall(html)
    # print(len(src_list))
    for src in src_list:
        #"//pic.qiushibaike.com/system/pictures/12064/120645061/medium/app120645061.jpeg"
        # 去掉图片链接两边的双引号
        src = src.strip('"')
        img_url = 'https:' + src
        download_img(img_url)

def build_url(url, page):
    url = url + str(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'

    }
    req = urllib.request.Request(url=url, headers=headers)
    return req

def main():
    url = 'https://www.qiushibaike.com/pic/'
    start_page = int(input('请输入起始页码: '))
    end_page = int(input('请输入结束页码: '))
    print('开始下载')
    for page in range(start_page, end_page+1):
        req = build_url(url, page)
        get_content(req)


if __name__ == '__main__':
    main()