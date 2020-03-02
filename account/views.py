from flask import Response, request, json
from flask.views import MethodView
from werkzeug.exceptions import BadRequestKeyError
import os
from settings.utils import api
from practice import macro
import threading


class Hooks(MethodView):
    def post(self):
        res = json.dumps(request.form)
        res = json.loads(res)
        res = json.loads(res['payload'])
        if res['ref'] == 'refs/heads/deploy':
            os.system('sh /home/ec2-user/yatigu-server/settings/hooks.sh')
        return Response('push', status=200)


class User(MethodView):
    @api
    def post(self, data):
        match_list = ['source', 'destination', 'year', 'month', 'day', 'hour', 'phone', 'pw', 'index']
        for key in match_list:
            if key not in data.keys():
                raise BadRequestKeyError  # data에 key가 올바르게 담겨있지 않음
        threading.Thread(target=macro.users.append_user, args=(data['source'], data['destination'],
                                                              data['year'], data['month'], data['day'], data['hour'],
                                                              data['phone'], data['pw'], data['index'])).start()
        return Response('running', status=200)
