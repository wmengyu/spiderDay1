
import urllib.request

url = 'https://weibo.com/u/5852893758/home?wvr=5&sudaref=graph.qq.com'

headers = {
    'Cookie': 'SINAGLOBAL=696526235126.4534.1530582916406; YF-Ugrow-G0=8751d9166f7676afdce9885c6d31cd61; login_sid_t=2ab621d591eddca04b205556d131562c; cross_origin_proto=SSL; YF-V5-G0=b8115b96b42d4782ab3a2201c5eba25d; WBStorage=5548c0baa42e6f3d|undefined; wb_view_log=1366*7681; _s_tentry=passport.weibo.com; Apache=362373836056.45544.1530673345160; ULV=1530673345170:2:2:2:362373836056.45544.1530673345160:1530582916430; WBtopGlobal_register_version=2e7679c973813872; crossidccode=CODE-gz-1FAy4g-15gTLl-i9bLB55jX9gejnk5d2bea; ALF=1562209380; SSOLoginState=1530673381; SUB=_2A252OEi2DeThGeNG7lAZ-S3LzjSIHXVVTD1-rDV8PUNbmtBeLWrDkW9NS1wBZkINRamrHshnD31v8PbjxSkm-VF1; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFb_SAxHARg.1T3IYWDEjD15JpX5KzhUgL.Fo-RSKzR1KeNSKn2dJLoI0qLxK-L1-BL12qLxK-LBKBLBK.LxKBLB.BLB.qLxKML1hnLBo2LxKqL122LB.BLxK.LBKeL12-t; SUHB=0JvwwKJ7FHgJl1; wvr=6; YF-Page-G0=c47452adc667e76a7435512bb2f774f3; '
              'wb_view_log_5852893758=1366*7681; UOR=,,graph.qq.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}

req = urllib.request.Request(url=url,headers=headers)
res = urllib.request.urlopen(req)
# print(res.read().decode('utf-8'))

with open('weibo1.html', 'wb') as fw:
    fw.write(res.read())

print(res.read().decode('utf-8'))