from flask.views import MethodView
from selenium import webdriver
from settings.settings import CHROME_DRIVER_PATH


# driver = webdriver.Chrome(CHROME_DRIVER_PATH)  # 로그인 전용으로 미리 열어놓는 크롬드라이버


class Login(MethodView):
    def get(self):
        return 'get'

    def post(self):
        return 'post'