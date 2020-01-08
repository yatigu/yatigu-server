from flask import Blueprint
from .views import Login

app = Blueprint('login', __name__)

login_view = Login.as_view('login_view')
app.add_url_rule('/', view_func=login_view)

