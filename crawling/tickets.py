from bs4 import BeautifulSoup
import requests


def tickets():
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
    print(res.text)

tickets()