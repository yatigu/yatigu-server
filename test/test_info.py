from datetime import datetime


def test_stations(client):  # 기차역을 불러온다.
    res = client.get('/info/stations/')
    assert res.status_code == 200


def test_tickets(client):  # 티켓 정보를 불러온다.
    data = {
        'date': str(datetime.now()).replace('-', '')[0:8],
        'hour': '235900',
        'start': '서울',
        'end': '부산'
    }
    res = client.get('/info/tickets/')  # data 없거나 안맞을경우
    assert res.status_code == 400
    res = client.get('/info/tickets/', data=data)
    assert res.status_code == 200


