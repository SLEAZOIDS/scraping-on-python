from selenium import webdriver
from bs4 import BeautifulSoup
import io,sys,os,time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

driver = webdriver.PhantomJS()

url = "https://www.yahoo.co.jp/"

driver.get(url)
driver.find_element_by_id('economy').click()

# クリック後のロードを待つ
time.sleep(1)

html = driver.page_source.encode('utf-8')
soup = BeautifulSoup(html, "html.parser")

nikkei_average = soup.find('dl', class_ = 'tpcdtlinfo').find('dd').text

print('******************************')

print(nikkei_average)

print('******************************')

# スクリーンショットテスト
driver.save_screenshot(os.path.dirname(os.path.abspath(__file__)) + "/yahoo.png")

driver.quit()