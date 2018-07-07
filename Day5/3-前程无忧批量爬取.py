import json
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

class QianChen(object):
    def __init__(self, url, work_post, start_page, end_page):
        super(QianChen, self).__init__()
        self.url = url
        self.work_post = work_post
        self.start_page = start_page
        self.end_page = end_page
        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.3'

        }
        self.items = []

    def build_url(self, page):
        data = {
            'work_post': self.work_post,
            'page': str(page)
        }
        url = self.url+urllib.parse.quote(data['work_post'])+',2,'+data['page']+'.html'
        req = urllib.request.Request(url=url, headers=self.headers)
        return req

    def download_data(self, req):
        res =urllib.request.urlopen(req)
        #构建bs4对象
        bs = BeautifulSoup(res.read(), 'lxml')
        table_list = bs.select('#resultList .el')[1:]
        for table in table_list:
            item = {}
            post = table.select('p a')[0].get_text()
            company = table.select('.t2 > a')[0].get_text()
            site = table.select('.t3')[0].get_text()
            salary = table.select('.t4')[0].get_text()
            start_time = table.select('.t5')[0].get_text()
            item['post'] = post.strip()
            item['company'] = company
            item['site'] = site
            item['salary'] = salary
            item['start_time'] = start_time
            self.items.append(item)



    #对外提供的接口函数
    def start(self):
        for page in range(self.start_page, self.end_page+1):
            req = self.build_url(page)
            self.download_data(req)
        #将python对象转化为json字符串
        json_str = json.dumps(self.items, ensure_ascii=False)
        #将json字符串写入到文件
        with open('qianchen.json', 'w', encoding='utf-8') as f:
            f.write(json_str)


def main():
    url = 'https://search.51job.com/list/130200,000000,0000,00,9,99,'
    work_post = input('请输入工作岗位: ')
    start_page = int(input('请输入开始页码: '))
    end_page = int(input('请输入结束页码: '))
    qc = QianChen(url, work_post, start_page, end_page)
    qc.start()

if __name__ == '__main__':
    main()