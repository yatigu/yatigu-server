from flask import request, jsonify, make_response
from flask.views import MethodView
from settings.serialize import serialize
from crawling.station import get_station
from functools import wraps
import json

class Station(MethodView):
    def get(self):
        station = get_station()
        res = {'station': {}}

        for index, data in enumerate(station):
            res['station'][str(index)] = data

        return jsonify(res)

