import urllib.request
import urllib.parse
import os
from lxml import etree


def download_img(url_list, name_list):
    dirpath = './hunsha'
    for i in range(len(name_list)):
        #获取后缀名
        suffix = os.path.splitext(url_list[i])[-1]
        #得到图片全路径
        file_path = os.path.join(dirpath, name_list[i])+suffix
        try:
            urllib.request.urlretrieve(url_list[i], file_path)
            print('%s-下载完毕' %file_path)
        except Exception as e:
            print('图片丢失')

def get_data(req):
    #发送请求
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf-8')
    html_etree = etree.HTML(html)
    url_list = html_etree.xpath('//div[@id="container"]/div/div/a/img/@src2')
    name_list = html_etree.xpath('//div[@id="container"]/div/div/a/img/@alt')
    download_img(url_list, name_list)

def build_req(url):
    headers = {
        'User - Agent':'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML,likeGecko)Chrome/65.0.3325.146Safari/537.36'
    }

    #创建请求
    req = urllib.request.Request(headers=headers, url=url)
    return req


def main():
    start_page = int(input('请输入起始页: '))
    end_page= int(input('请输入结束页码: '))
    url_tmp = 'http://sc.chinaz.com/tupian/hunsha'
    print('开始下载')
    for page in range(start_page, end_page+1):
        if page != 1:
            url = url_tmp+"_"+str(page)+'.html'
        else:
            url = url_tmp+'.html'
        #构建请求对象
        req = build_req(url)
        #获取数据
        get_data(req)



if __name__ == '__main__':
    main()