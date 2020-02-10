from flask import Blueprint

from account.views import Hooks

app = Blueprint('account', __name__)

#login_view = AccountUser.as_view('account_user_view')
#app.add_url_rule('/user/', view_func=login_view)
hooks_view = Hooks.as_view('hooks_view')
app.add_url_rule('/hooks/', view_func=hooks_view)
