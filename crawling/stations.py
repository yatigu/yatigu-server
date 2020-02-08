import requests


def get_station():
    url = 'http://www.letskorail.com/docs/js/pr/autocomplete_stations.js?v=20200201'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.146 Whale/2.6.90.16 Safari/537.36'}
    res = requests.get(url, headers=headers)
    station = res.text.split('\n')
    station_array = []

    for i in station:
        if i.startswith('stationArr'):
            station_arr = (i[17:].replace('\'', '').replace(';', '').replace('[', '').replace(']', '').replace('\'', '').split(','))
            for k, j in enumerate(station_arr):
                station_arr[k] = j.strip()
            station_array.append(station_arr)

    return station_array


