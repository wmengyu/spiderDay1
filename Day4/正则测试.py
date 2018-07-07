import re

str1='<div>哈哈<div>呵呵</div>拉拉<div>嘻嘻</div>嘿嘿</div>'
res1 = re.match('<div>>.*?</div>', str1)
print(res1)


#子模式
str2 = 'goodgood678studeny99'
res2 = re.match('good(\d+)study', str2)
print(res2)
print(res2.group)