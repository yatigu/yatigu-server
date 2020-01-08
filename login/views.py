from flask.views import MethodView

class Login(MethodView):
    def get(self):
        return 'get'

    def post(self):
        return 'post'