import threading

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from settings.settings import CHROME_DRIVER_PATH


class Korail:  # 코레일 매크로 클래스
    class Ticket_info:  # 티켓 정보를 담고있는 클래스
        def __init__(self, source='서울', destination='부산', year='2020', month='02', day='10', hour='23',
                     index='1', phone='01012341234', pw='1234!'):
            self.source = source  # 출발지
            self.destination = destination  # 목적지
            self.year = year  # 해당 년도
            self.month = month  # 해당 월
            self.day = day  # 해당 일
            self.hour = hour
            self.index = index
            self.phone = phone
            self.pw = pw

    def __init__(self, source='서울', destination='부산', year='2020', month='01', day='29', hour='15', index='1', phone='01012341234', pw='1234!'):
        self.driver = None
        self.is_ = False
        self.ticket_info = self.Ticket_info(source, destination, year, month, day, hour, index, phone, pw)  # 티켓 정보를 담아줌
        self.korail_url = 'http://www.letskorail.com/korail/com/login.do'  # 로그인창 주소
        self.chrome_driver_path = CHROME_DRIVER_PATH  # 크롬드라이버 경로
        self.book_url = 'http://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do'  # 예매창 주소

        self.make_driver()  # 드라이버를 셋팅함
        self.login()  # 로그인

    def repeat(self):  # 반복시킬 함수
        try:
            self.book_ticket()  # 티켓 예매
            alert = self.driver.switch_to_alert()
            alert.accept()
        except Exception as e:  # 예매 실패
            pass
        else:  # 예매 성공
            self.is_ = True
            self.driver.quit()

    def chrome_options(self):  # 크롬 드라이버에 옵션을 추가하는 함수
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # 창 안띄우고 진행
        chrome_options.add_argument("disable-infobars")  # info message 안띄움
        chrome_options.add_argument("start-maximized")  # 나머지 옵션은 잘 모르겠는데 빨라진다는 말이있어서 씀
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--no-sandbox")  # bypass OS security model
        chrome_options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        return chrome_options

    def make_driver(self):  # 크롬 드라이버를 연동하고 코레일로 이동하는 함수
        self.driver = webdriver.Chrome(
            executable_path=self.chrome_driver_path, chrome_options=self.chrome_options())  # 드라이버에 옵션 적용
        self.move_url(self.korail_url)  # 로그인 페이지로 이동

    def login(self):  # 로그인하는 함수
        self.click_element('//*[@title="휴대전화번호 로그인"]')  # 휴대전화 번호로 로그인 클릭
        self.send_keys('//*[@title="휴대전화 중간자리"]', self.ticket_info.phone[3:7])  # 중간자리 입력
        self.send_keys('//*[@title="휴대전화 끝자리"]', self.ticket_info.phone[7:])  # 끝자리 입력
        self.send_keys('//*[@name="txtPwd1"]', self.ticket_info.pw + Keys.ENTER)  # 비밀번호 입력 후 엔터

    def book_ticket(self):  # 예매하는 과정을 처리하는 함수
        self.driver.get(self.book_url)  # 티켓 검색 페이지로 이동
        self.clear('//*[@name="txtGoStart"]')  # 출발지에 써있는거 지움
        self.send_keys('//*[@name="txtGoStart"]', self.ticket_info.source)  # 출발지 입력
        self.clear('//*[@name="txtGoEnd"]')  # 도착지에 써있는거 지움
        self.send_keys('//*[@name="txtGoEnd"]', self.ticket_info.destination)  # 목적지 입력
        self.select('//*[@name="selGoYear"]', self.ticket_info.year)  # 년도 선택
        self.select('//*[@name="selGoMonth"]', self.ticket_info.month)  # 월 선택
        self.select('//*[@name="selGoDay"]', self.ticket_info.day)  # 일 선택
        self.select('//*[@name="selGoHour"]', self.ticket_info.hour)
        self.click_element('//*[@alt="조회하기"]')  # 조회하기 클릭
        self.click_element(f'/html/body/div[1]/div[3]/div/div[1]/form[1]/div/div[4]/table[1]/tbody/tr[{self.ticket_info.index}]/td[6]/a[1]/img')

    def click_element(self, path):  # 해당 엘리먼트를 클릭하는 함수
        self.driver.find_element_by_xpath(path).click()  # 휴대전화로 로그인 클릭
        self.driver.implicitly_wait(3)  # 위의 작동을 최대 3초까지 기다려줌

    def send_keys(self, path, input_string):  # 해당 엘리먼트에 스트링을 입력하는 함수
        self.driver.find_element_by_xpath(path).send_keys(input_string)  # 휴대전화로 로그인 클릭
        self.driver.implicitly_wait(3)

    def move_url(self, path):  # URL을 이동하는 함수
        self.driver.get(path)  # 해당 URL로 이동
        self.driver.implicitly_wait(3)

    def clear(self, path):  # 해당 엘리먼트의 텍스트를 초기화하는 함수
        self.driver.find_element_by_xpath(path).clear()  # 해당 패스의 입력값을 지움
        self.driver.implicitly_wait(3)

    def select(self, path, value):  # 셀렉터에서 선택하는 함수
        Select(self.driver.find_element_by_xpath(path)).select_by_value(value)  # 해당 셀렉터의 벨류를 선택함
        self.driver.implicitly_wait(3)


class UserManagement:  # 유저를 관리하기 위한 클래스
    def __init__(self):
        self.users_array = []  # 유저의 세션을 저장하기 위한 리스트
        self.amount_of_users = 0

    def append_user(self, source='서울', destination='부산',
                    year='2020', month='02', day='10', hour='12',
                    phone='01012341234', pw='1234!', index='1'):  # 유저를 어레이에 추가하는 함수
        self.amount_of_users += 1
        user = Korail(source=source, destination=destination,
                      year=year, month=month, day=day, hour=hour,
                      phone=phone, pw=pw, index=index)  # 유저를 생성
        self.users_array.append(user)  # users에 user를 추가함


users = UserManagement()  # 유저 관리 오브젝트 생성


def repeat():
    while True:
        try:
            if len(users.users_array) > 0:
                for user in users.users_array:
                    user.repeat()
                    if user.is_:
                        users.users_array.remove(user)
                        users.amount_of_users -= 1
        except KeyboardInterrupt:
            break


threading.Thread(target=repeat).start()



