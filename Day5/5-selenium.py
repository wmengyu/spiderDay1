# #加载驱动
# import time
#
# from selenium import webdriver
#
#
# #通过驱动构建操作浏览器对象
# browser = webdriver.Chrome()
# #要打开的页码
# open_url = 'https://www.baidu.com'
# #执行打开动作
# browser.get(open_url)
# #休眠2秒
# time.sleep(3)
# #根据元素id查找
# b_setting = browser.find_element_by_xpath('//[@id="ul"]/a[8]/text()')
# b_setting.click()
# time.sleep(3)
#
#
#
#
# browser.quit()
#
#



import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# browser = webdriver.Chrome('./chromedriver.exe')
browser = webdriver.Chrome()

open_url = 'https://www.baidu.com'



browser.get(open_url)
time.sleep(5)

browser.maximize_window()
setting = browser.find_element_by_xpath('//*[@id="u1"]/a[8]')
ActionChains(browser).move_to_element(setting).perform()
time.sleep(2)

ha = browser.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]')
ha.click()
time.sleep(2)

b_input = browser.find_element_by_css_selector('#kw')
#输入字符
b_input.send_keys('美女')
time.sleep(3)
b_submit = browser.find_element_by_id('su')
#进行点击动作
b_submit.click()
time.sleep(3)