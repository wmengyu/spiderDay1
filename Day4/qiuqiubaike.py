import json
import os

from lxml import etree
import urllib.request
import urllib.parse

# #发送请求
# def download_img(img_url, name_list):
#     dirpath = './qiuqiubaike'
#     #获取后缀名
#     img_name = os.path.basename(img_url)
#     #得到图片全路径
#     file_path = os.path.join(dirpath, img_name)
#     try:
#         urllib.request.urlretrieve(img_url, file_path, name_list)
#         print('%s-下载完毕' %file_path)
#     except Exception as e:
#         print('图片丢失')


def get_data(req):
    res=urllib.request.urlopen(req)
    html = res.read().decode('utf-8')
    #得到document对象
    html_etree = etree.HTML(html)

    url_list = html_etree.xpath('//div[@class="author clearfix"]/a[1]/img/@src')
    name_list = html_etree.xpath('//div[@class="author clearfix"]/a[1]/img[1]/@alt')
    title_list = html_etree.xpath('//div[@class="author clearfix"]/a[2]/h2/text()')
    list = []
    for i in range(len(name_list)):
        data = {}
        imgs = url_list[i]
        names = name_list[i]
        titles = title_list[i]
        data['imgs'] = imgs
        data['names'] = names
        data[titles] = titles
        list.append(data)
    return list

def write(list):
    with open('data.json', 'a+', encoding='utf-8') as f:
        f.write(json.dumps(list))

#创建请求
def build_req(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.3'

    }
    req = urllib.request.Request(url=url,headers=headers)
    return req

def main():
    start_page = int(input('请输入起始页: '))
    end_page = int(input('请输入结束页: '))
    url_tmp = 'https://www.qiushibaike.com/text/'
    list1 = []
    print('开始下载')
    for page in range(start_page, end_page+1):
        if page != 1:
            url = url_tmp+'page/'+str(page)
        else:
            url = url_tmp
        #构建请求对象
        req = build_req(url)
        get_data(req)
        list1.append(list)
    write(list1)


if __name__ == '__main__':
    main()