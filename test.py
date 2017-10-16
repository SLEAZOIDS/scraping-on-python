from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS()
driver.get("https://www.yahoo.co.jp/")
data = driver.page_source.encode('utf-8')

print(data)
driver.save_screenshot("ss.png")

driver.quit()