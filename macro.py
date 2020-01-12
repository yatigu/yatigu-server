from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import time
from multiprocessing import Pool

chrome_options = Options()
chrome_options.add_argument("--headless")  # 창 안띄우고 진행
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")


driver = webdriver.Chrome(executable_path='C:\chromedriver.exe', chrome_options=chrome_options)  # 드라이버에 옵션 적용
driver.implicitly_wait(3)
start = time.time()
def test():
    for i in range(10):
        driver.get('http://www.letskorail.com/korail/com/login.do')  # 로그인 페이지로 이동
        driver.implicitly_wait(3)
        driver.find_element_by_xpath('//*[@title="휴대전화번호 로그인"]').click()  # 휴대전화로 로그인 클릭
        driver.find_element_by_xpath('//*[@title="휴대전화 중간자리"]').send_keys('4028')  # 전화번호 입력
        driver.find_element_by_xpath('//*[@title="휴대전화 끝자리"]').send_keys('2628')  # 전화번호 입력
        driver.find_element_by_name('txtPwd1').send_keys('rhrnak2628!'+Keys.ENTER)  # 비밀번호 입력

        driver.implicitly_wait(3)
        driver.get('http://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do')  # 티켓 조회 페이지로 이동
        driver.implicitly_wait(3)
        driver.find_element_by_name('txtGoStart').clear()
        driver.find_element_by_name('txtGoStart').send_keys('서울')  # 출발지 입력
        driver.find_element_by_name('txtGoEnd').clear()
        driver.find_element_by_name('txtGoEnd').send_keys('부산')  # 도착지 입력
        Select(driver.find_element_by_name('selGoYear')).select_by_value('2020')  # 조회 날짜
        Select(driver.find_element_by_name('selGoMonth')).select_by_value('01')
        Select(driver.find_element_by_name('selGoDay')).select_by_value('13')
        driver.find_element_by_xpath('//*[@alt="조회하기"]').click()  # 조회 클릭
        driver.implicitly_wait(3)
        print(driver.find_element_by_xpath('//*[@id="tableResult"]')\
            .text)  # 임시코드임 여기는 얘기좀해봐야함
        driver.find_element_by_xpath('//*[@alt="로그아웃"]').click()  # 다음 유저를 위해 로그아웃
        Alert(driver).accept()  # 로그아웃 얼럴트창 수락
        driver.implicitly_wait(3)

driver.close()
print(time.time()-start)
