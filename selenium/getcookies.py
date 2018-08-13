#coding:utf-8
from selenium import webdriver
import time
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"]) 
driver = webdriver.Chrome(chrome_options=options) 

driver=webdriver.Chrome()
driver.get("https://www.cnblogs.com")
print driver.get_cookies()
print("----------------------------")
#登录后获取cookies
url = "https://passport.cnblogs.com/user/signin"
driver.get(url)
driver.implicitly_wait(30)
driver.find_element_by_id("input1").send_keys(u"怕几眼木马你海哥")
driver.find_element_by_id("input2").send_keys(u"xmxel9516.")
driver.find_element_by_id("signin").click()
time.sleep(3)
print driver.get_cookies()
print("----------------------------")
#获取指定的cookie
print driver.get_cookie(name=".CNBlogsCookie")
