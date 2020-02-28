def test_user(client):
    res = client.post('/account/user/')
    assert res.status_code == 400

    data = {
        'phone': '01012341234',
        'pw': '01012341234',
        'index': '3',
        'source': '서울',
        'destination': '부산',
        'year': '2020',
        'month': '03',
        'day': '09',
        'hour': '15'
    }
    res = client.post('/account/user/', data=data)
    assert res.status_code == 200
