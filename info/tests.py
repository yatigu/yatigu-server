import requests
from datetime import datetime

url = 'http://15.165.170.3:8000'


def test_stations():  # 기차역을 불러온다.
    res = requests.get(f'{url}/info/stations/')
    assert res.status_code == 200


def test_tickets():  # 티켓 정보를 불러온다.
    data = {
        'date': str(datetime.now()).replace('-', '')[0:8],
        'hour': '235900',
        'start': '서울',
        'end': '부산'
    }
    res = requests.get(f'{url}/info/tickets')  # data 없거나 안맞을경우
    assert res.status_code == 400
    res = requests.get(f'{url}/info/tickets', data=data)
    assert res.status_code == 200


