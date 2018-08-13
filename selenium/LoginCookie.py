#coding:utf-8
from selenium import webdriver
import time
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"]) 
driver = webdriver.Chrome(chrome_options=options) 

driver=webdriver.Chrome()
driver.get("https://www.cnblogs.com")


c1={
	u'domain': u'.cnblogs.com',
	u'expiry': 1533612270, 
	u'secure': False,
	u'path': u'/', 
	u'httpOnly': False,
	u'name':u'.CNBlogsCookie',
    u'value':u'37A00D55B7F9A74E55DB4F7F49A350973BD10C30E546117A9A31C29B77EE129B5B964F13C52B0D9B29117DE37E8E47BD822B97E470209C98E35DEC08F96AFD10CB9F0980910A4507B9675C54037B53B7EECE299B',
   }
c2={
	u'domain': u'.cnblogs.com',
	u'expiry': 1533612270, 
	u'secure': False,
	u'path': u'/', 
	u'httpOnly': False,
	u'name':u'.Cnblogs.AspNetCore.Cookies',
	u'value':u'CfDJ8FHXRRtkJWRFtU30nh_M9mApoI_16k00OuZ8dM1fDAwm0j-M4DFejElrfiXW78g3HzTkXYKsaA1VYkbspMEi_WFvMNL1bXZV-GERI8exX4V3IAKCYBhfgjfXeD_fZMO-W0z0MwAhXGl7T6ZvdjQuCwhJYfj1sNGD5_IQy_FFmEmBNYsbAYsdcixmRLzY51gbnJ2WfUymtnFeyj1udIyaC2swjMLwFoVCstSreWJJpTi0yGdhwgZqmMsOzQVHp4-0cKPQXeJcY6EhR2GTB59YDSw8oPVjRa_ZjDHJuJOoAUxVKILHT4twPqAQRm0--TqsOwem1w8Tx88HwvGHGtL2sEM'
}

driver.add_cookie(c1)
driver.add_cookie(c2)

time.sleep(3)

driver.refresh()