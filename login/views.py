from flask.views import MethodView
from selenium import webdriver
from settings.settings import CHROME_DRIVER_PATH


driver = webdriver.Chrome(CHROME_DRIVER_PATH)  # 로그인 전용으로 미리 열어놓는 크롬드라이버


class Login(MethodView):
    def get(self):
        driver.get('http://www.naver.com/')  # 샘플코드. 컨트롤 가능한지 테스트.
        return 'get'

    def post(self):
        return 'post'