'''
모든 앱의 접근 주소를 여기서 관리함.
여기에서 반드시 임포트와 레지스터 해줘야함.
앱에서만 유알엘을 추가한다고 적용되지 않음.
'''

from settings.settings import app
from login import urls as loginurls
from account import urls as accounturls

app.register_blueprint(loginurls.app, url_prefix='/login')  # /login으로 시작하면 login_app으로 연결
app.register_blueprint(accounturls.app, url_prefix='/account')