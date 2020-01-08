from flask import Blueprint
from .views import AccountUser
app = Blueprint('account', __name__)

login_view = AccountUser.as_view('account_user_view')
app.add_url_rule('/user/', view_func=login_view)