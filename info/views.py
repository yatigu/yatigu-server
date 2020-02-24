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
        keys = list()  # key 검사
        for key in data.keys():
            keys.append(key)
        if 'date' and 'hour' and 'start' and 'end' not in keys:
            raise BadRequestKeyError  # key가 올바르지 않음
        return jsonify(get_tickets(data['date'], data['hour'], data['start'], data['end']))

    @api
    def post(self, data):
        keys = list()  # key 검사
        for key in data.keys():
            keys.append(key)
        if 'date' and 'hour' and 'start' and 'end' not in keys:
            raise BadRequestKeyError  # key가 올바르지 않음
        return jsonify(get_tickets(data['date'], data['hour'], data['start'], data['end']))

