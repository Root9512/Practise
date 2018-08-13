# coding:utf-8
from bs4 import BeautifulSoup
import requests

r = requests.get("http://www.cnblogs.com/yoyoketang/mvc/blog/sidecolumn.aspx?blogApp=yoyoketang")

blog = r.content

soup = BeautifulSoup(blog, "html.parser")
tag_soup = soup.find(class_="catListTag")

# print body.prettify()

ul_soup = tag_soup.find_all("a")
print ul_soup
for i in ul_soup:
    print i.string