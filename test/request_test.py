from selenium.webdriver.chrome.options import Options
from seleniumrequests import Chrome
from time import time

start = time()
chrome_options = Options()
chrome_options.add_argument("--headless")  # 창 안띄우고 진행
# chrome_options.add_argument("disable-infobars")
# chrome_options.add_argument("start-maximized")
# chrome_options.add_argument("--disable-extensions")
driver = Chrome(executable_path='C:\chromedriver.exe', options=chrome_options)
res = driver.request('GET', 'http://www.letskorail.com/korail/com/login.do')
print(time()-start)
res = driver.request('GET', 'http://www.letskorail.com/korail/com/login.do')
print(time()-start)
res = driver.request('GET', 'http://www.letskorail.com/korail/com/login.do')
print(time()-start)
res = driver.request('GET', 'http://www.letskorail.com/korail/com/login.do')
print(time()-start)
res = driver.request('GET', 'http://www.letskorail.com/korail/com/login.do')
print(time()-start)
res = driver.request('GET', 'http://www.letskorail.com/korail/com/login.do')
print(time()-start)

driver.implicitly_wait(3)
# print(res)
driver.close()
print(time()-start)