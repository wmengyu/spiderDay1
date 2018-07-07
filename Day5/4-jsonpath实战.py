import json

# fr =open('book_store.json','r',encoding='utf-8')
# json_str=fr.read()
# fr.close()
# json_obj=json.loads(json_str)

#以上步骤可以一步搞定
import jsonpath

json_obj = json.load(open('book_store.json','r',encoding='utf-8'))
# print(json_obj)
# print(type(json_obj))
#获取所有作者
result =jsonpath.jsonpath(json_obj,'$.store.book[*].author')
result =jsonpath.jsonpath(json_obj,'$..author')
#获取所有价格
result =jsonpath.jsonpath(json_obj,'$.store..price')

#获取最后一本书
result =jsonpath.jsonpath(json_obj,'$..book[(@.length-1)]')

#前面2本书
result =jsonpath.jsonpath(json_obj,'$..book[:2]')
result =jsonpath.jsonpath(json_obj,'$..book[0,1]')
print(result)
print(result[1])