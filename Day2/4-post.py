import json
import urllib.request
import urllib.parse

url = 'http://fanyi.baidu.com/sug/'

headers = {
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}

kw=input('请输入要查询的词:')

data ={
    'kw':kw
}
#编码动作
data=urllib.parse.urlencode(data).encode('utf-8')
#构建请求
req=urllib.request.Request(url=url,headers=headers,data=data)
#发送请求
res=urllib.request.urlopen(req)
#读取响应数据
result=res.read().decode('utf-8')
#把json字符串转为python对象
json_obj=json.loads(result)
#把python对象转为json字符串
str=json.dumps(json_obj,ensure_ascii=False)
# print(result)
#进行写入操作
with open('baidufy.json','w',encoding='utf-8') as fw:
    fw.write(str)