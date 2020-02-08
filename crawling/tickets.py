from bs4 import BeautifulSoup


def tickets(html):
    bs = BeautifulSoup(html, 'lxml')
    tickets = bs.find_all('tbody')

