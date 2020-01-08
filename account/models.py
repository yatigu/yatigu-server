from settings.settings import db


class User(db.Model):
    __tablename__ = 'user_info'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    user_phone = db.Column(db.String(30), primary_key=True, unique=True)  # 휴대전화번호
    user_pw = db.Column(db.String(30))  # 비밀번호
    user_status = db.Column(db.String(30), default='STOP')  # 서비스 사용중인지 현재 상태

    def __init__(self, user_phone, user_pw, user_status):
        self.user_phone = user_phone
        self.user_pw = user_pw
        self.user_status = user_status

    def __repr__(self):
        return 'user_phone : {}, user_pw : {}, user_status : {}'.format(self.user_phone, self.user_pw, self.user_name)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}


