from flask import jsonify
from flask.views import MethodView
from crawling.stations import get_stations
from crawling.tickets import get_tickets


class Stations(MethodView):
    def get(self):
        station = get_stations()
        res = {'stations': {}}

        for index, data in enumerate(station):
            res['stations'][str(index)] = data

        return jsonify(res)


class Tickets(MethodView):
    def get(self):
        return jsonify(get_tickets())

