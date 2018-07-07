#获得文档对象
from  lxml import etree
#构建document对象
d_tree=etree.parse('testXpath.html')
# print(d_tree)
#1-获取所有的li节点
# res=d_tree.xpath('//li')
# # #2-获取所有li节点的class属性
# res=d_tree.xpath('//li/@class')
#3-获取每一个ol节点最后一个li节点的文本内容
# res=d_tree.xpath('//ol/li[last()]/text()')
# #3-获取每一个ol节点最后一个li节点的最后一个文本内容
# res=d_tree.xpath('//ol/li[last()]/text()')[2]
#4-拿到http://mi.com值
# res=d_tree.xpath('//div[@class="hh"]/a/@href')[0]
# #5-拿到雷军文本值
# res=d_tree.xpath('//div[@class="hh"]/a/text()')[0]
# #6-找到id为pp的div中ol节点里面class以h开头的li节点
# res=d_tree.xpath('//div[@id="pp"]/ol/li[starts-with(@class,"h")]')
# #7-找到id为pp的div中ol节点里面class以h开头的第2个li节点文本
res=d_tree.xpath('//div[@id="pp"]/ol/li[starts-with(@class,"h")]/text()')[1]
print(res)