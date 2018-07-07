import urllib.parse
import urllib.request



#编码
str=urllib.parse.quote('http://www.baidu.com?name=中国')
print(str)
#解码

str1=urllib.parse.unquote('http%3A//www.baidu.com%3Fname%3D%E4%B8%AD%E5%9B%BD')
print(str1)