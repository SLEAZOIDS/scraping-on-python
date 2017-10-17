from selenium import webdriver
from bs4 import BeautifulSoup
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

driver = webdriver.PhantomJS()

url = "http://www.nikkei.com/"
# url = "https://www.yahoo.co.jp/"

driver.get(url)
html = driver.page_source.encode('utf-8')

soup = BeautifulSoup(html, "html.parser")

title_tag = soup.title
title = title_tag.string

print('******************************')

print(title_tag)

print('******************************')

print(title)

print('******************************')

driver.save_screenshot("ss.png")

driver.quit()