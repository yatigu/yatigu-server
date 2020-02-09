from bs4 import BeautifulSoup
import requests


def get_tickets():
    params = {
        'selGoTrain': '05',
        'radJobId': '1',
        'checkStnNm': 'Y',
        'txtGoAbrdDt': '20200210',
        'txtGoHour': '160000',
        'txtGoStart': '서울',
        'txtGoEnd': '부산',

    }
    res = requests.post('http://www.letskorail.com/ebizprd/EbizPrdTicketPr21111_i1.do', params=params)
    bs = BeautifulSoup(res.text, 'lxml')
    table = bs.find_all('tr')

    info = {'tickets': {}}
    for index, value in enumerate(table):
        if index == 0 or index == 11:
            continue
        find_tr = value.find_all('td')
        print(index)
        ticket_items = {}
        for i, v in enumerate(find_tr):
            if i == 0:
                table_key = '구분'
                ticket_items[table_key] = (v.text.replace('\t', '').replace('\n', '').replace('\r', '').strip())
            elif i == 1:
                table_key = '열차번호'
                ticket_items[table_key] = (v.text.replace('\t', '').replace('\n', '').replace('\r', '').strip())
            elif i == 2:
                table_key = '출발시간'
                ticket_items[table_key] = (v.text.replace('\t', '').replace('\n', '').replace('\r', '').strip())
            elif i == 3:
                table_key = '도착시간'
                ticket_items[table_key] = (v.text.replace('\t', '').replace('\n', '').replace('\r', '').strip())
        info['tickets'][str(index)] = ticket_items

    return info
