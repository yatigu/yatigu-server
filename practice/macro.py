from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from requests import Session

from crawling.tickets import get_tickets
from settings.settings import CHROME_DRIVER_PATH
from time import sleep


class Korail():  # 코레일 매크로 클래스
    class Ticket_info():  # 티켓 정보를 담고있는 클래스
        def __init__(self, source='서울', destination='부산', year='2020', month='02', day='10'):
            self.source = source  # 출발지
            self.destination = destination  # 목적지
            self.year = year  # 해당 년도
            self.month = month  # 해당 월
            self.day = day  # 해당 일

    def __init__(self, source='서울', destination='부산', year='2020', month='01', day='29'):
        self.driver = None
        self.ticket_info = self.Ticket_info(source, destination, year, month, day)  # 티켓 정보를 담아줌
        self.korail_url = 'http://www.letskorail.com/korail/com/login.do'  # 로그인창 주소
        self.chrome_driver_path = CHROME_DRIVER_PATH  # 크롬드라이버 경로
        self.book_url = 'http://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do'  # 예매창 주소

        self.make_driver()  # 드라이버를 셋팅함
        self.login()  # 로그인
        #self.logout()  # 로그아웃
        self.book_ticket()  # 티켓 예매
        #self.driver.close()  # 드라이버 종료  # todo 실제 동작시킬땐 지워야함

    def chrome_options(self):  # 크롬 드라이버에 옵션을 추가하는 함수
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # 창 안띄우고 진행
        chrome_options.add_argument("disable-infobars")  # info message 안띄움
        chrome_options.add_argument("start-maximized")  # 나머지 옵션은 잘 모르겠는데 빨라진다는 말이있어서 씀
        chrome_options.add_argument("--disable-extensions")
        return chrome_options

    def make_driver(self):  # 크롬 드라이버를 연동하고 코레일로 이동하는 함수
        self.driver = webdriver.Chrome(
            executable_path=self.chrome_driver_path, options=self.chrome_options())  # 드라이버에 옵션 적용
        self.move_url(self.korail_url)  # 로그인 페이지로 이동

    def get_cookie(self):  # todo 쓰게되면 코드 정리할것.
        session = Session()
        for cookie in self.driver.get_cookies():
            session.cookies.set('domain', cookie['domain'])
            session.cookies.set('httpOnly', cookie['httpOnly'])
            session.cookies.set('name', cookie['name'])
            session.cookies.set('path', cookie['path'])
            session.cookies.set('secure', cookie['secure'])
            session.cookies.set('value', cookie['value'])
            print(cookie)
        print(session.cookies.get_dict())

    def login(self):  # 로그인하는 함수
        self.click_element('//*[@title="휴대전화번호 로그인"]')  # 휴대전화 번호로 로그인 클릭
        self.send_keys('//*[@title="휴대전화 중간자리"]', '4028')  # 중간자리 입력
        self.send_keys('//*[@title="휴대전화 끝자리"]', '2628')  # 끝자리 입력
        self.send_keys('//*[@name="txtPwd1"]', 'rhrnak2628!' + Keys.ENTER)  # 비밀번호 입력 후 엔터

    def book_ticket(self):  # 예매하는 과정을 처리하는 함수
        self.move_url(self.book_url)  # 티켓 검색 페이지로 이동
        self.clear('//*[@name="txtGoStart"]')  # 출발지에 써있는거 지움
        self.send_keys('//*[@name="txtGoStart"]', self.ticket_info.source)  # 출발지 입력
        self.clear('//*[@name="txtGoEnd"]')  # 도착지에 써있는거 지움
        self.send_keys('//*[@name="txtGoEnd"]', self.ticket_info.destination)  # 목적지 입력
        self.select('//*[@name="selGoYear"]', self.ticket_info.year)  # 년도 선택
        self.select('//*[@name="selGoMonth"]', self.ticket_info.month)  # 월 선택
        self.select('//*[@name="selGoDay"]', self.ticket_info.day)  # 일 선택
        self.click_element('//*[@alt="조회하기"]')  # 조회하기 클릭

    def logout(self):
        self.driver.find_element_by_xpath('//*[@alt="로그아웃"]').click()  # 다음 유저를 위해 로그아웃
        self.driver.implicitly_wait(3)
        Alert(self.driver).accept()  # 로그아웃 얼럴트창 수락
        self.driver.implicitly_wait(3)

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


class User_management():  # 유저를 관리하기 위한 클래스
    def __init__(self):
        self.users_array = []  # 유저의 세션을 저장하기 위한 리스트

    def append_user(self, source='서울', destination='부산',
                    year='2020', month='02', day='10'):  # 유저를 어레이에 추가하는 함수
        user = Korail(source=source, destination=destination, year=year, month=month, day=day)  # 유저를 생성
        self.users_array.append(user)  # users에 user를 추가함


if __name__ == '__main__':
    users = User_management()  # 유저 관리 오브젝트 생성
    users.append_user()  # 유저 추가
    # users.append_user()  # 유저 추가
    '''
    위의 방식으로 유저들을 생성한 뒤 아래의 방식으로 컨트롤 해준다.
    유저를 생성할 때 드라이버를 연동시키는 과정에서 시간이 오래걸리기 때문에 생성하는건 스레드를 따로돌리면 좋을듯.
    이후의 과정은 메인 스레드에서 처리하는데 만~~약 유저 수가 늘어난다면 서버를 증설하거나 스레드를 나눠서 처리해줘야할듯.
    
    full xpath로 첫번째 버튼을 클릭하는 방식으로 생각하려고함.
    시간을 정확하게 입력하여 인덱스로 버튼을 찾는다고 생각하면됨.
    검색해서 나오는 기차표들중 맨 위에서부터 1로 시작함.
    '''
    # for user in users.users_array:  # 유저를 컨트롤함
    #     user.move_url('http://www.google.com')
    #     user.send_keys('//*[@title="검색"]', 'asdq3wkejk')
    #
    #     user.move_url('http://www.google.com')
    #     user.send_keys('//*[@title="검색"]', 'asdq3wkejk')

