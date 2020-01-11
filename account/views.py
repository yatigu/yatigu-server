from flask import request, jsonify
from flask.views import MethodView
from settings.serialize import serialize
from .models import User, db


class AccountUser(MethodView):
    def get(self):
        get_user = db.session.query(User).\
            filter(User.user_phone == request.form['user_phone']).first()  # user_id로 검색해서 가져옴
        if get_user is None:  # 해당하는 정보가 없음
            return jsonify(), 400

        return jsonify(serialize(get_user)), 200

    def post(self):
        # try:
        new_user = User(user_phone=request.form['user_phone'],  # 리퀘스트로 정보를 생성해서 저장함
                        user_pw=request.form['user_pw'],
                        user_status=request.form['user_status'],
                        user_rank=request.form['user_rank'])
        db.session.add(new_user)
        db.session.commit()
        # except:  # 이미 존재하는 정보(규칙 어긋남)
        #     return jsonify(), 400

        return jsonify(serialize(new_user)), 200

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
        return jsonify(serialize(get_user)), 200
