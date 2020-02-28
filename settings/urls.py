'''
모든 앱의 접근 주소를 여기서 관리함.
여기에서 반드시 임포트와 레지스터 해줘야함.
앱에서만 유알엘을 추가한다고 적용되지 않음.
'''

from settings.settings import app
from account import urls as accounturls
from info import urls as infourls

app.register_blueprint(accounturls.app, url_prefix='/account')
app.register_blueprint(infourls.app, url_prefix='/info')
