import json
from time import sleep
import pandas as pd
import sqlalchemy
from settings.settings import POSTGRESQL
'''
ORM으로 바꾸고싶다
'''
url = POSTGRESQL  # postgresql 주소
engine = sqlalchemy.create_engine(url, client_encoding='utf8')
user_list = []  # 서비스 이용자 리스트

if __name__ == '__main__':
    while True:  # 전체 과정을 계속해서 반복함
        result = json.loads(pd.read_sql('select * from user_info', engine)\
                            .to_json())  # 이용자 정보를 db에서 json으로 받음
        for i in range(len(result['user_phone'])):  # 이용자 수 만큼 반복함
            '''
            이 반복문 안에 패킷 날리는게 들어갈꺼임.
            아직 코레일 패킷 안뜯어봤음.
            '''
            print(result['user_phone'][str(i)])


        sleep(1)
# with requests.Session() as s:
#     id = request.data.get('id')
#     pw = request.data.get('pw')
#     URL = 'https://ktis.kookmin.ac.kr/kmu/com.Login.do?'
#
#     data = {'txt_user_id': id, 'txt_passwd': pw}
#
#     response = s.post(URL, data)