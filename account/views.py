'''from flask import request, jsonify
from flask.views import MethodView
from settings.serialize import serialize
from .models import User, db
import test.macro as Manager


manager = Manager.User_management()
class AccountUser(MethodView):
    def get(self):
        print(serialize(manager.users_array[0]))

        return jsonify({}), 200

    def post(self):

        manager.append_user()

        return jsonify({}), 200

    def delete(self):
        get_user = db.session.query(User).filter(User.user_phone == request.form['user_phone']).first()
        if get_user is None:  # 해당하는 정보가 없음
            return jsonify(), 400
        db.session.delete(get_user)
        db.session.commit()
        return jsonify(serialize(get_user)), 200

    def put(self):
        get_user = db.session.query(User).filter(User.user_phone == request.form['user_phone']).first()
        if get_user is None:  # 해당하는 정보가 없음
            return jsonify(), 400
        get_user.user_status = request.form['user_status']  # 유저의 상태를 수정
        db.session.commit()
        if request.form['user_status'] == 'RUN':  # 유저가 서비스를 이용하는 상태로 바뀌면
            user_list.append(get_user)  # 유저 리스트에 해당 유저를 추가한다.
        return jsonify(serialize(get_user)), 200
'''
from flask import Response, request, json
from flask.views import MethodView
import practice.macro as macro
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
        t1 = threading.Thread(target=macro.users.append_user, args=(data['source'], data['destination'],
                                                              data['year'], data['month'], data['day'], data['hour'],
                                                              data['phone'], data['pw'], data['index'])).start()
        return Response('running', status=200)
