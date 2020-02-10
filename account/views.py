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
import os


class Hooks(MethodView):
    def post(self):

        print(request.headers)
        print(request.form['ref'])
        os.system('sh /home/ec2-user/yatigu-server/settings/hooks.sh')

        return Response('push', status=200)
