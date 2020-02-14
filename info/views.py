from flask import jsonify, request, Response, json
from flask.views import MethodView
from crawling.stations import get_stations
from crawling.tickets import get_tickets
from settings.utils import headers


class Stations(MethodView):
    def get(self):
        station = get_stations()
        res = {'stations': {}}

        for index, data in enumerate(station):
            res['stations'][str(index)] = data
        json_obj = json.dumps(res)
        return Response(json_obj, headers=headers, status=200)


class Tickets(MethodView):
    def get(self):
        try:
            request.form['date']
            request.form['hour']
            request.form['start']
            request.form['end']
        except KeyError:
            return Response(status=400)
        return jsonify(get_tickets(request.form['date'], request.form['hour'], request.form['start'], request.form['end']))

