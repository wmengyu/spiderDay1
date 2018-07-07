#创建bs对象
import bs4
from bs4 import BeautifulSoup

#创建bs对象
bs = BeautifulSoup(open('1-bs4_test.html'), 'lxml')
#找到a标签和title
result = bs.a
result = bs.title

#节点属性attrs
# $节点属性attrs  列出属性  返回一个字典
res1=result.attrs
print(res1)
#获取节点属性值(3种方式)
print(res1.get('href'))
print(res1['href'])

# 获取节点内容
print(result.sting)
print(result.get_text())

#判断是否是注释内容
if type(result.string == bs4.element.Comment):
    print('是注释内容')
else:
    print('不是注释内容')


#获取body的直接子节点
print(len(bs.body.contents))


#获取body的直接子孙节点
print(type(bs.body.descendants))

for tag in bs.body.descendants:
    print(tag)


#find find_all select

print(bs.find('a'))
print(bs.find('a', title="出塞"))
print(bs.find('a', id="hong"))
#注意class的写法
print(bs.find('a', class_="taohua"))


print(bs.find_all('a'))
print(bs.find_all('a')[3])
print(bs.find_all('a', limit=1))  #第一个

print(bs.find_all(['a', 'span']))


#层级选择器和属性选择器
print(bs.select('div[class="tang"] a[class="taohu"]')) #返回一个列表

print(bs.select('div[class="tang"] a[name="he"]'))

