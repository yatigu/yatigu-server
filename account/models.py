from settings.settings import db


class User(db.Model):
    __tablename__ = 'user_info'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    user_id = db.Column(db.String(30), primary_key=True, unique=True)
    user_pw = db.Column(db.String(30))
    user_name = db.Column(db.String(30))

    def __init__(self, user_id, user_pw, user_name):
        self.user_id = user_id
        self.user_pw = user_pw
        self.user_name = user_name

    def __repr__(self):
        return 'user_id : {}, user_pw : {}, user_name : {}'.format(self.user_id, self.user_pw, self.user_name)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}


