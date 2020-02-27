from flask import jsonify, request
from flask.views import MethodView
from werkzeug.exceptions import BadRequestKeyError
from crawling.stations import get_stations
from crawling.tickets import get_tickets
from settings.utils import api


class Stations(MethodView):
    def get(self):
        station = get_stations()
        res = {'stations': {}}

        for index, data in enumerate(station):
            res['stations'][str(index)] = data
        return jsonify(res)


class Tickets(MethodView):
    @api
    def get(self, data):
        match_list = ['date', 'hour', 'start', 'end']
        for key in match_list:
            if key not in data.keys():
                raise BadRequestKeyError  # data에 key가 올바르게 담겨있지 않음

        return jsonify(get_tickets(data['date'], data['hour'], data['start'], data['end']))



